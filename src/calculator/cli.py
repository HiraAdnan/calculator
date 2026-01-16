"""
Command-line interface module.

Provides the interactive calculator CLI:
- format_result: Format numeric results for display
- is_exit_command: Check if user wants to exit
- main: Main interactive loop
"""

from calculator.operations import calculate
from calculator.parser import parse_number, parse_operation


def format_result(value: float) -> str:
    """
    Format a numeric result for display.

    Strips trailing zeros and unnecessary decimal points.

    Args:
        value: Float value to format

    Returns:
        Formatted string representation
    """
    formatted = f"{value:.10f}"
    formatted = formatted.rstrip("0").rstrip(".")
    return formatted


def is_exit_command(value: str) -> bool:
    """
    Check if input is an exit command.

    Args:
        value: User input string

    Returns:
        True if user wants to exit, False otherwise
    """
    return value.strip().lower() in {"quit", "exit"}


def get_number(prompt: str) -> float | None:
    """
    Get a valid number from user input.

    Args:
        prompt: The prompt to display

    Returns:
        Float value if valid, None if user wants to exit
    """
    while True:
        user_input = input(prompt)
        if is_exit_command(user_input):
            return None

        result = parse_number(user_input)
        if isinstance(result, str):
            print(result)
            continue
        return result


def get_operation() -> str | None:
    """
    Get a valid operation from user input.

    Returns:
        Operation symbol if valid, None if user wants to exit
    """
    while True:
        user_input = input("Enter operation (+, -, *, /): ")
        if is_exit_command(user_input):
            return None

        result = parse_operation(user_input)
        if result.startswith("Error"):
            print(result)
            continue
        return result


def main() -> None:
    """Main interactive calculator loop."""
    print("Simple Calculator")
    print("Type 'quit' or 'exit' to close")
    print()

    while True:
        # Get first number
        num1 = get_number("Enter first number: ")
        if num1 is None:
            break

        # Get operation
        op = get_operation()
        if op is None:
            break

        # Get second number
        num2 = get_number("Enter second number: ")
        if num2 is None:
            break

        # Calculate and display result
        result = calculate(num1, op, num2)
        if isinstance(result, str):
            print(result)
        else:
            print(f"Result: {format_result(result)}")
        print()

    print("Goodbye!")


if __name__ == "__main__":
    main()
