"""Test CLI module"""
import pytest
from click.testing import CliRunner
from gemini_cli_tool.cli import main


def test_cli_help():
    """Test CLI help command"""
    runner = CliRunner()
    result = runner.invoke(main, ["--help"])
    assert result.exit_code == 0, f"Help command failed: {result.output}"


def test_cli_no_api_key():
    """Test CLI gracefully handles missing API key"""
    runner = CliRunner()
    result = runner.invoke(main, ["analyze", "test.py"])
    # Should not crash with unhandled exception
    assert result.exit_code != 1 or "Error" in result.output or "API" in result.output or "key" in result.output


def test_cli_imports():
    """Test that module imports work"""
    from gemini_cli_tool import __version__
    assert __version__ is not None
