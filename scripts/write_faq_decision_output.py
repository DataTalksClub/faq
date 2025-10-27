#!/usr/bin/env python3
"""
GitHub Actions helper script to write FAQ decision output

Reads faq_decision.json and writes to GitHub Actions GITHUB_OUTPUT.
"""

import json
import sys
from pathlib import Path

# Add parent directory to path to import faq_automation
sys.path.insert(0, str(Path(__file__).parent.parent))

from faq_automation.github_actions import write_github_output


def main():
    """Main entry point"""
    try:
        # Read FAQ decision from file
        decision_file = Path('/tmp/faq_decision.json')

        if not decision_file.exists():
            print("Error: FAQ decision file not found at /tmp/faq_decision.json", file=sys.stderr)
            sys.exit(1)

        with open(decision_file) as f:
            decision = json.load(f)

        # Write as compact JSON (single line)
        decision_json = json.dumps(decision)
        write_github_output('decision', decision_json, multiline=False)

        print("✅ Successfully wrote FAQ decision to GitHub Actions output")
        print(f"   Action: {decision.get('action', 'unknown')}")

    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in FAQ decision file: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
