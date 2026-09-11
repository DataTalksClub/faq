# Opik integration

We trace the FAQ automation with Opik and score it with Opik experiments.
The local eval framework (`faq_automation/evals/`) stays the source of truth;
Opik mirrors it. To go back, delete the Opik files and env vars below.

## Platforms

|  | Opik Cloud (shared, Friday demos) | Local (private dev) |
|---|---|---|
| URL | `https://www.comet.com/opik/api` | `http://localhost:5173/api` (`cd ../opik && ./opik.sh`) |
| Workspace | `default` | `default` |
| Auth | `OPIK_API_KEY` (GitHub secret in CI, never in git) | none |
| Automation project | `faq-automation-ci` | `faq-automation` |
| Assistant project | `faq-assistant-lambda` | `faq-assistant` |

## Tracing

`faq_automation/rag_agent.py` (full SDK, 2 lines + 1 decorator):

```python
from opik import track
from opik.integrations.openai import track_openai

self.openai_client = track_openai(OpenAI(api_key=openai_api_key))

@track
def process_proposal(self, ...): ...
```

The Slack worker (`faq-assistant`, separate repo) intentionally does NOT ship
the SDK — Lambda stays zero-dependency. It uses a ~140-line stdlib-only
`@track` drop-in (`opik_lite.py`) that POSTs one trace per answer. Same
annotation, one-line import swap.

## Evals on Opik

`faq_automation/evals/opik_eval.py` (additive port, same cases and check
predicates as `runner.py`):

```bash
source .env  # OPIK_API_KEY
# push cases once:
OPIK_URL_OVERRIDE=https://www.comet.com/opik/api OPIK_WORKSPACE=default \
  OPIK_PROJECT_NAME=faq-automation-ci \
  uv run --project faq_automation python -m faq_automation.evals.opik_eval --push-dataset
# before/after (deterministic action_match + placement_match, no judge cost):
uv run --project faq_automation python -m faq_automation.evals.opik_eval \
  --experiment friday-before --num-results 1
uv run --project faq_automation python -m faq_automation.evals.opik_eval \
  --experiment friday-after --num-results 5
```

## Prompts in Opik

We do NOT load prompts from Opik — `rag_agent.SYSTEM_PROMPT` and
`PROMPT_TEMPLATE` remain the single source of truth. We mirror them into the
Prompt Library so every version sits next to the traces/experiments that used
it. Re-running with unchanged templates creates no new version:

```bash
OPIK_URL_OVERRIDE=https://www.comet.com/opik/api OPIK_WORKSPACE=default \
  OPIK_PROJECT_NAME=faq-automation-ci \
  uv run --project faq_automation python scripts/push_prompts_to_opik.py
```

Library entries: `faq-triage-system`, `faq-triage-user-template`
(metadata records the source symbol and the model from `DEFAULT_MODEL`).

## History backfill

`scripts/backfill_opik_history.py` logs past `faq-proposal` issues as
`faq-proposal-triage` traces with real timestamps: input = original issue +
regenerated retrieval context, output = the actual historical decision from
the bot PR or close comment (or MANUAL). `--dry-run` first, `--limit N` to
bound it.

## CI wiring

`.github/workflows/faq-automation.yml` ("Process FAQ with AI" step) sets
`OPIK_URL_OVERRIDE` / `OPIK_WORKSPACE` / `OPIK_PROJECT_NAME=faq-automation-ci`
and `OPIK_API_KEY` from secrets. Without a key the SDK degrades to no-op —
automation never breaks because of tracing.
