"""
Flex processing for the eval runner.

Flex bills at the same discounted rate as the Batch API but answers in real time.
The catch is that individual requests are slower and can be turned away with a 429
when capacity is tight, so we retry with backoff and run cases concurrently to get
the wall-clock time back. For evals that trade is free: nobody is watching a single
case, but everybody is watching the suite.

Use this while iterating. Batch is the better fit when the whole suite can wait.
"""

import random
import time
from concurrent.futures import ThreadPoolExecutor

from openai import APIStatusError, APITimeoutError, RateLimitError

from faq_automation.rag_agent import FAQDecision, extract_decision

MAX_ATTEMPTS = 5
MAX_WORKERS = 8


def request(client, messages, model, max_attempts=MAX_ATTEMPTS):
    """
    Send one proposal on the flex tier, retrying capacity errors with backoff.

    Falls back to the standard tier on the last attempt rather than losing the
    case: a scored case at full price beats a hole in the results.
    """
    for attempt in range(max_attempts):
        last_attempt = attempt == max_attempts - 1
        tier = 'auto' if last_attempt else 'flex'

        try:
            response = client.responses.parse(
                model=model,
                input=messages,
                text_format=FAQDecision,
                service_tier=tier,
            )
            return extract_decision(response)
        except (RateLimitError, APITimeoutError) as e:
            if last_attempt:
                raise
            backoff = 2 ** attempt + random.random()
            print(f"  [retry] {type(e).__name__}, sleeping {backoff:.1f}s")
            time.sleep(backoff)
        except APIStatusError as e:
            if last_attempt or e.status_code < 500:
                raise
            backoff = 2 ** attempt + random.random()
            print(f"  [retry] HTTP {e.status_code}, sleeping {backoff:.1f}s")
            time.sleep(backoff)


def collect(client, prepared, model, max_workers=MAX_WORKERS):
    """
    Run every prepared case on the flex tier concurrently.

    Returns decisions in `prepared` order, with None for any case that never
    came back, so the caller can fail it instead of silently dropping it.
    """
    def run(item):
        case, agent, _ = item
        messages = agent.build_messages(case.question, case.answer)
        try:
            return request(client, messages, model)
        except Exception as e:
            print(f"  [error] issue #{case.issue_number}: {type(e).__name__}: {e}")
            return None

    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        return list(pool.map(run, prepared))
