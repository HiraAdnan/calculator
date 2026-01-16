"""Tests for calculator.cli module."""

import pytest

from calculator.cli import format_result, is_exit_command


# =============================================================================
# User Story 2: Decimal Number Support (T025-T026)
# =============================================================================

class TestFormatResult:
    """Tests for format_result() function."""

    def test_format_decimal_result(self) -> None:
        """T025: Test formatting decimal result."""
        assert format_result(2.5) == "2.5"

    def test_format_strips_trailing_zeros(self) -> None:
        """T026: Test formatting strips trailing zeros."""
        assert format_result(8.0) == "8"

    def test_format_negative(self) -> None:
        """Test formatting negative numbers."""
        assert format_result(-5.0) == "-5"

    def test_format_zero(self) -> None:
        """Test formatting zero."""
        assert format_result(0.0) == "0"

    def test_format_long_decimal(self) -> None:
        """Test formatting long repeating decimal."""
        result = format_result(3.3333333333)
        assert result.startswith("3.333")


# =============================================================================
# Phase 7: CLI Integration (T047-T048)
# =============================================================================

class TestIsExitCommand:
    """Tests for is_exit_command() function."""

    def test_is_exit_command_quit(self) -> None:
        """T047: Test quit is recognized as exit command."""
        assert is_exit_command("quit") is True

    def test_is_exit_command_exit(self) -> None:
        """Test exit is recognized as exit command."""
        assert is_exit_command("exit") is True

    def test_is_exit_command_case_insensitive(self) -> None:
        """T048: Test exit commands are case insensitive."""
        assert is_exit_command("QUIT") is True
        assert is_exit_command("EXIT") is True
        assert is_exit_command("Quit") is True
        assert is_exit_command("Exit") is True

    def test_is_exit_command_not_exit(self) -> None:
        """Test non-exit commands return False."""
        assert is_exit_command("q") is False
        assert is_exit_command("5") is False
        assert is_exit_command("+") is False
        assert is_exit_command("") is False
