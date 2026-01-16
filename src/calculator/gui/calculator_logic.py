"""
Calculator state management.

Bridges UI events to core operations module.
"""

from calculator.operations import calculate
from calculator.cli import format_result


class CalculatorState:
    """
    Manages calculator state and bridges UI events to core operations.

    Attributes:
        display_value: Current value shown on display
        first_operand: Stored first operand (after operation pressed)
        pending_operation: Operation waiting for second operand
        waiting_for_operand: Whether next digit starts new number
    """

    def __init__(self) -> None:
        """Initialize calculator state."""
        self.display_value: str = "0"
        self.first_operand: float | None = None
        self.pending_operation: str | None = None
        self.waiting_for_operand: bool = False

    def digit_pressed(self, digit: str) -> str:
        """
        Handle digit (0-9) button press.

        Args:
            digit: The digit pressed

        Returns:
            New display value
        """
        if self.waiting_for_operand:
            self.display_value = digit
            self.waiting_for_operand = False
        else:
            if self.display_value == "0":
                self.display_value = digit
            else:
                self.display_value += digit
        return self.display_value

    def decimal_pressed(self) -> str:
        """
        Handle decimal point press.

        Returns:
            New display value
        """
        if self.waiting_for_operand:
            self.display_value = "0."
            self.waiting_for_operand = False
        elif "." not in self.display_value:
            self.display_value += "."
        return self.display_value

    def operation_pressed(self, op: str) -> str:
        """
        Handle operation (+, -, *, /) press.

        Args:
            op: Operation symbol

        Returns:
            Display value (may show intermediate result)
        """
        current = float(self.display_value)

        if self.first_operand is not None and not self.waiting_for_operand:
            result = calculate(self.first_operand, self.pending_operation or "+", current)
            if isinstance(result, str):
                self.clear_pressed()
                return result
            self.display_value = format_result(result)
            self.first_operand = result
        else:
            self.first_operand = current

        self.pending_operation = op
        self.waiting_for_operand = True
        return self.display_value

    def equals_pressed(self) -> str:
        """
        Calculate result.

        Returns:
            Result or error message
        """
        if self.first_operand is None or self.pending_operation is None:
            return self.display_value

        second = float(self.display_value)
        result = calculate(self.first_operand, self.pending_operation, second)

        if isinstance(result, str):
            self.clear_pressed()
            return result

        self.display_value = format_result(result)
        self.first_operand = None
        self.pending_operation = None
        self.waiting_for_operand = True
        return self.display_value

    def clear_pressed(self) -> str:
        """
        Clear all state.

        Returns:
            '0'
        """
        self.display_value = "0"
        self.first_operand = None
        self.pending_operation = None
        self.waiting_for_operand = False
        return "0"

    def negate_pressed(self) -> str:
        """
        Toggle positive/negative.

        Returns:
            New display value
        """
        current = float(self.display_value)
        self.display_value = format_result(-current)
        return self.display_value

    def backspace_pressed(self) -> str:
        """
        Remove last digit.

        Returns:
            New display value
        """
        if len(self.display_value) > 1:
            self.display_value = self.display_value[:-1]
            if self.display_value == "-":
                self.display_value = "0"
        else:
            self.display_value = "0"
        return self.display_value
