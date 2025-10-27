"""
Unit tests for GitHub Actions integration helpers
"""

import os
import pytest
import tempfile
from pathlib import Path

from faq_automation.github_actions import (
    write_github_output,
    get_github_output_path,
    is_github_actions,
)


class TestWriteGithubOutput:
    """Test the write_github_output function"""

    def test_write_github_output_multiline(self):
        """Test writing multiline output to GitHub Actions"""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            temp_path = f.name

        try:
            # Set GITHUB_OUTPUT environment variable
            os.environ['GITHUB_OUTPUT'] = temp_path

            # Write multiline output
            write_github_output('test_key', 'line1\nline2\nline3', multiline=True)

            # Read back and verify
            with open(temp_path) as f:
                content = f.read()

            assert 'test_key<<EOF\n' in content
            assert 'line1\nline2\nline3\n' in content
            assert 'EOF\n' in content

        finally:
            if 'GITHUB_OUTPUT' in os.environ:
                del os.environ['GITHUB_OUTPUT']
            Path(temp_path).unlink()

    def test_write_github_output_single_line(self):
        """Test writing single-line output to GitHub Actions"""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            temp_path = f.name

        try:
            # Set GITHUB_OUTPUT environment variable
            os.environ['GITHUB_OUTPUT'] = temp_path

            # Write single-line output
            write_github_output('test_key', 'single_value', multiline=False)

            # Read back and verify
            with open(temp_path) as f:
                content = f.read()

            assert content == 'test_key=single_value\n'
            assert 'EOF' not in content

        finally:
            if 'GITHUB_OUTPUT' in os.environ:
                del os.environ['GITHUB_OUTPUT']
            Path(temp_path).unlink()

    def test_write_github_output_no_env_var(self, capsys):
        """Test behavior when GITHUB_OUTPUT is not set (local testing mode)"""
        # Ensure GITHUB_OUTPUT is not set
        if 'GITHUB_OUTPUT' in os.environ:
            del os.environ['GITHUB_OUTPUT']

        # Write output (should print to stdout)
        write_github_output('test_key', 'test_value', multiline=False)

        # Capture stdout
        captured = capsys.readouterr()
        assert 'test_key: test_value' in captured.out

    def test_write_github_output_multiline_no_env_var(self, capsys):
        """Test multiline output when GITHUB_OUTPUT is not set"""
        # Ensure GITHUB_OUTPUT is not set
        if 'GITHUB_OUTPUT' in os.environ:
            del os.environ['GITHUB_OUTPUT']

        # Write multiline output (should print to stdout)
        write_github_output('test_key', 'line1\nline2', multiline=True)

        # Capture stdout
        captured = capsys.readouterr()
        assert 'test_key:' in captured.out
        assert 'line1' in captured.out
        assert 'line2' in captured.out

    def test_write_github_output_multiple_calls(self):
        """Test multiple sequential writes to GitHub Actions output"""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            temp_path = f.name

        try:
            # Set GITHUB_OUTPUT environment variable
            os.environ['GITHUB_OUTPUT'] = temp_path

            # Write multiple outputs
            write_github_output('key1', 'value1', multiline=False)
            write_github_output('key2', 'value2\nvalue3', multiline=True)
            write_github_output('key3', 'value4', multiline=False)

            # Read back and verify
            with open(temp_path) as f:
                content = f.read()

            assert 'key1=value1\n' in content
            assert 'key2<<EOF\n' in content
            assert 'value2\nvalue3\n' in content
            assert 'key3=value4\n' in content

        finally:
            if 'GITHUB_OUTPUT' in os.environ:
                del os.environ['GITHUB_OUTPUT']
            Path(temp_path).unlink()


class TestGetGithubOutputPath:
    """Test the get_github_output_path function"""

    def test_get_github_output_path_set(self):
        """Test getting path when GITHUB_OUTPUT is set"""
        try:
            os.environ['GITHUB_OUTPUT'] = '/tmp/test_output'
            path = get_github_output_path()
            assert path == '/tmp/test_output'
        finally:
            if 'GITHUB_OUTPUT' in os.environ:
                del os.environ['GITHUB_OUTPUT']

    def test_get_github_output_path_not_set(self):
        """Test getting path when GITHUB_OUTPUT is not set"""
        if 'GITHUB_OUTPUT' in os.environ:
            del os.environ['GITHUB_OUTPUT']
        path = get_github_output_path()
        assert path is None


class TestIsGithubActions:
    """Test the is_github_actions function"""

    def test_is_github_actions_true(self):
        """Test detection when running in GitHub Actions"""
        try:
            os.environ['GITHUB_ACTIONS'] = 'true'
            assert is_github_actions() is True
        finally:
            if 'GITHUB_ACTIONS' in os.environ:
                del os.environ['GITHUB_ACTIONS']

    def test_is_github_actions_false(self):
        """Test detection when not running in GitHub Actions"""
        if 'GITHUB_ACTIONS' in os.environ:
            del os.environ['GITHUB_ACTIONS']
        assert is_github_actions() is False

    def test_is_github_actions_wrong_value(self):
        """Test detection with incorrect GITHUB_ACTIONS value"""
        try:
            os.environ['GITHUB_ACTIONS'] = 'false'
            assert is_github_actions() is False
        finally:
            if 'GITHUB_ACTIONS' in os.environ:
                del os.environ['GITHUB_ACTIONS']
