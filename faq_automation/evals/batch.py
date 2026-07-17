"""
Batch API plumbing for the eval runner.

Eval cases are independent requests and nobody is waiting on the answer, which
is exactly what the Batch API is for: same requests, half the price, results
within 24h (in practice a few minutes).

The flow is: build a JSONL file with one request per case, upload it, submit the
job, poll until it reaches a terminal state, then download and parse the results.
Each request carries a custom_id so results map back to their case regardless of
the order they come back in.
"""

import json
import time
from typing import Optional

from faq_automation.rag_agent import FAQDecision, RESPONSE_TEXT_FORMAT

ENDPOINT = "/v1/responses"

TERMINAL_STATUSES = {"completed", "failed", "expired", "cancelled"}


def build_request(custom_id: str, messages: list, model: str) -> dict:
    """Build one JSONL line: the same request process_proposal would send live."""
    return {
        "custom_id": custom_id,
        "method": "POST",
        "url": ENDPOINT,
        "body": {
            "model": model,
            "input": messages,
            "text": {"format": RESPONSE_TEXT_FORMAT},
        },
    }


def submit(client, requests: list, input_path) -> str:
    """Write the JSONL file, upload it, and create the batch job. Returns batch id."""
    lines = []
    for request in requests:
        lines.append(json.dumps(request))
    input_path.write_text('\n'.join(lines) + '\n', encoding='utf-8')

    with open(input_path, 'rb') as f:
        input_file = client.files.create(file=f, purpose='batch')

    batch = client.batches.create(
        input_file_id=input_file.id,
        endpoint=ENDPOINT,
        completion_window='24h',
        metadata={'description': 'faq merge agent evals'},
    )
    return batch.id


def poll(client, batch_id: str, interval: int = 15, timeout: Optional[int] = None):
    """Poll the batch until it reaches a terminal state. Returns the batch object."""
    started = time.monotonic()

    while True:
        batch = client.batches.retrieve(batch_id)
        counts = batch.request_counts
        elapsed = int(time.monotonic() - started)
        print(f"  [{elapsed:>4}s] {batch.status}: {counts.completed}/{counts.total} completed, {counts.failed} failed")

        if batch.status in TERMINAL_STATUSES:
            return batch

        if timeout is not None and time.monotonic() - started > timeout:
            raise TimeoutError(f"batch {batch_id} still {batch.status} after {timeout}s")

        time.sleep(interval)


def fetch(client, batch) -> dict:
    """
    Download the results file and parse each line.

    Returns:
        {custom_id: FAQDecision} for requests that succeeded. Failed requests are
        reported and left out, so the caller can fail their cases explicitly rather
        than silently scoring a partial run as a pass.
    """
    if not batch.output_file_id:
        raise RuntimeError(f"batch {batch.id} finished as {batch.status} with no output file")

    decisions = {}
    content = client.files.content(batch.output_file_id).text

    for line in content.splitlines():
        if not line.strip():
            continue

        result = json.loads(line)
        custom_id = result['custom_id']

        if result.get('error'):
            print(f"  [error] {custom_id}: {result['error']}")
            continue

        response = result['response']
        if response['status_code'] != 200:
            print(f"  [error] {custom_id}: HTTP {response['status_code']}")
            continue

        decisions[custom_id] = parse_decision(response['body'])

    return decisions


def parse_decision(body: dict) -> FAQDecision:
    """Pull the structured output text out of a Responses API body."""
    for item in body['output']:
        if item.get('type') != 'message':
            continue
        for chunk in item['content']:
            if chunk.get('type') == 'output_text':
                return FAQDecision.model_validate_json(chunk['text'])

    raise ValueError("no output_text found in response body")
