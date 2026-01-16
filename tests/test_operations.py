"""Tests for calculator.operations module."""

import pytest

from calculator.operations import add, subtract, multiply, divide, calculate


# =============================================================================
# User Story 1: Basic Arithmetic Operations (T011-T015)
# =============================================================================

class TestAdd:
    """Tests for add() function."""

    def test_add_integers(self) -> None:
        """T011: Test addition of two positive integers."""
        assert add(5, 3) == 8

    def test_add_zero(self) -> None:
        """Test addition with zero."""
        assert add(0, 0) == 0
        assert add(5, 0) == 5
        assert add(0, 5) == 5

    # US2: Decimal support
    def test_add_decimals(self) -> None:
        """T023: Test addition of decimal numbers."""
        assert add(3.14, 2.5) == pytest.approx(5.64)

    # US3: Negative numbers
    def test_add_negative(self) -> None:
        """T032: Test addition with negative numbers."""
        assert add(-5, 3) == -2


class TestSubtract:
    """Tests for subtract() function."""

    def test_subtract_integers(self) -> None:
        """T012: Test subtraction of two positive integers."""
        assert subtract(10, 4) == 6

    def test_subtract_larger_from_smaller(self) -> None:
        """Test subtraction resulting in negative number."""
        assert subtract(5, 8) == -3


class TestMultiply:
    """Tests for multiply() function."""

    def test_multiply_integers(self) -> None:
        """T013: Test multiplication of two positive integers."""
        assert multiply(5, 3) == 15

    def test_multiply_by_zero(self) -> None:
        """Test multiplication by zero."""
        assert multiply(5, 0) == 0
        assert multiply(0, 5) == 0

    # US3: Negative numbers
    def test_multiply_negatives(self) -> None:
        """T033: Test multiplication of two negatives."""
        assert multiply(-5, -3) == 15


class TestDivide:
    """Tests for divide() function."""

    def test_divide_integers(self) -> None:
        """T014: Test division of two integers with exact result."""
        assert divide(10, 2) == 5.0

    def test_divide_zero_numerator(self) -> None:
        """Test division with zero numerator."""
        assert divide(0, 5) == 0.0

    # US2: Decimal result
    def test_divide_decimal_result(self) -> None:
        """T024: Test division resulting in decimal."""
        assert divide(10, 4) == 2.5

    # US3: Negative numbers
    def test_divide_negative(self) -> None:
        """T034: Test division with negative number."""
        assert divide(-10, 2) == -5.0

    # US4: Error handling
    def test_divide_by_zero(self) -> None:
        """T037: Test division by zero returns error string."""
        result = divide(5, 0)
        assert isinstance(result, str)
        assert "Cannot divide by zero" in result


class TestCalculate:
    """Tests for calculate() dispatch function."""

    def test_calculate_dispatch(self) -> None:
        """T015: Test calculate() routes to correct operation."""
        assert calculate(5, "+", 3) == 8.0
        assert calculate(10, "-", 4) == 6.0
        assert calculate(5, "*", 3) == 15.0
        assert calculate(10, "/", 2) == 5.0

    # US4: Error handling
    def test_calculate_invalid_operation(self) -> None:
        """T041: Test calculate with invalid operation."""
        result = calculate(5, "%", 3)
        assert isinstance(result, str)
        assert "Invalid operation" in result
