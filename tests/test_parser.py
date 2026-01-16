"""Tests for calculator.parser module."""

import pytest

from calculator.parser import parse_number, parse_operation


# =============================================================================
# User Story 2: Decimal Number Support (T022)
# =============================================================================

class TestParseNumber:
    """Tests for parse_number() function."""

    def test_parse_decimal(self) -> None:
        """T022: Test parsing decimal numbers."""
        assert parse_number("3.14") == 3.14
        assert parse_number("0.5") == 0.5

    # US3: Negative numbers
    def test_parse_negative(self) -> None:
        """T030: Test parsing negative integers."""
        assert parse_number("-5") == -5.0

    def test_parse_negative_decimal(self) -> None:
        """T031: Test parsing negative decimals."""
        assert parse_number("-3.14") == -3.14

    # US4: Error handling
    def test_parse_invalid_input(self) -> None:
        """T038: Test parsing invalid input returns error."""
        result = parse_number("abc")
        assert isinstance(result, str)
        assert "Invalid input" in result

    def test_parse_empty_input(self) -> None:
        """T039: Test parsing empty input returns error."""
        result = parse_number("")
        assert isinstance(result, str)
        assert "enter a value" in result

    def test_parse_whitespace(self) -> None:
        """Test parsing whitespace-only input."""
        result = parse_number("   ")
        assert isinstance(result, str)
        assert "enter a value" in result


# =============================================================================
# User Story 4: Error Handling (T040)
# =============================================================================

class TestParseOperation:
    """Tests for parse_operation() function."""

    def test_parse_valid_operations(self) -> None:
        """Test valid operation symbols."""
        assert parse_operation("+") == "+"
        assert parse_operation("-") == "-"
        assert parse_operation("*") == "*"
        assert parse_operation("/") == "/"

    def test_parse_invalid_operation(self) -> None:
        """T040: Test invalid operation returns error."""
        result = parse_operation("%")
        assert isinstance(result, str)
        assert "Invalid operation" in result

    def test_parse_empty_operation(self) -> None:
        """Test empty operation input."""
        result = parse_operation("")
        assert isinstance(result, str)
        assert "enter a value" in result
