"""Test CLI module"""
import pytest
from click.testing import CliRunner
from gemini_cli_tool.cli import main


def test_cli_help():
    """Test CLI help command"""
    runner = CliRunner()
    result = runner.invoke(main, ["--help"])
    assert result.exit_code == 0
    assert "Gemini" in result.output or "gemini" in result.output


def test_cli_version():
    """Test CLI version command"""
    runner = CliRunner()
    result = runner.invoke(main, ["--version"])
    assert result.exit_code == 0 or "version" in result.output.lower()
