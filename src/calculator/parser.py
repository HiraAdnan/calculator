"""
Input parsing module.

Provides functions for parsing and validating user input:
- parse_number: Parse string input into float with validation
- parse_operation: Validate operation symbol
"""

VALID_OPERATIONS = {"+", "-", "*", "/"}


def parse_number(value: str) -> float | str:
    """
    Parse a string into a float.

    Args:
        value: String input from user

    Returns:
        Parsed float on success, or error string on failure
    """
    stripped = value.strip()

    if not stripped:
        return "Error: Please enter a value"

    try:
        return float(stripped)
    except ValueError:
        return "Error: Invalid input - please enter a number"


def parse_operation(value: str) -> str:
    """
    Validate an operation symbol.

    Args:
        value: String input from user

    Returns:
        Validated operation symbol, or error string on failure
    """
    stripped = value.strip()

    if not stripped:
        return "Error: Please enter a value"

    if stripped in VALID_OPERATIONS:
        return stripped

    return "Error: Invalid operation - use +, -, *, or /"
