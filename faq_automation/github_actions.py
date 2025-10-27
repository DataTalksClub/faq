"""
GitHub Actions integration helpers

Provides utilities for writing outputs and interacting with GitHub Actions.
"""

import os
from typing import Optional


def write_github_output(key: str, value: str, multiline: bool = True) -> None:
    """
    Write output to GitHub Actions in the appropriate format

    Args:
        key: Output key name
        value: Output value
        multiline: If True, use heredoc format for multiline values.
                   If False, use simple key=value format for single-line values.

    Note:
        When GITHUB_OUTPUT environment variable is not set (local testing),
        outputs are printed to stdout instead.
    """
    github_output = os.environ.get('GITHUB_OUTPUT')

    if not github_output:
        # Local testing mode - print to stdout
        if multiline and '\n' in value:
            print(f"{key}:")
            for line in value.split('\n'):
                print(f"  {line}")
        else:
            print(f"{key}: {value}")
        return

    with open(github_output, 'a') as f:
        if multiline:
            # Heredoc format for multiline values
            # See: https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#multiline-strings
            f.write(f"{key}<<EOF\n{value}\nEOF\n")
        else:
            # Simple format for single-line values
            f.write(f"{key}={value}\n")


def get_github_output_path() -> Optional[str]:
    """
    Get the path to the GitHub Actions output file

    Returns:
        Path to GITHUB_OUTPUT file, or None if not in GitHub Actions context
    """
    return os.environ.get('GITHUB_OUTPUT')


def is_github_actions() -> bool:
    """
    Check if running in GitHub Actions environment

    Returns:
        True if running in GitHub Actions, False otherwise
    """
    return os.environ.get('GITHUB_ACTIONS') == 'true'
