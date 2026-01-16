"""
Arithmetic operations module.

Provides pure functions for basic arithmetic operations:
- add: Addition of two numbers
- subtract: Subtraction of two numbers
- multiply: Multiplication of two numbers
- divide: Division of two numbers (with division by zero handling)
- calculate: Dispatch function to route operations
"""


def add(a: float, b: float) -> float:
    """
    Add two numbers.

    Args:
        a: First operand
        b: Second operand

    Returns:
        Sum of a and b
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """
    Subtract second number from first.

    Args:
        a: First operand (minuend)
        b: Second operand (subtrahend)

    Returns:
        Difference (a - b)
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers.

    Args:
        a: First operand
        b: Second operand

    Returns:
        Product of a and b
    """
    return a * b


def divide(a: float, b: float) -> float | str:
    """
    Divide first number by second.

    Args:
        a: Numerator
        b: Denominator

    Returns:
        Quotient (a / b) on success, or error string if b is zero
    """
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


def calculate(a: float, op: str, b: float) -> float | str:
    """
    Perform the specified operation on two numbers.

    Args:
        a: First operand
        op: Operation symbol (+, -, *, /)
        b: Second operand

    Returns:
        Result of operation, or error string for invalid operation
    """
    if op == "+":
        return add(a, b)
    elif op == "-":
        return subtract(a, b)
    elif op == "*":
        return multiply(a, b)
    elif op == "/":
        return divide(a, b)
    else:
        return "Error: Invalid operation - use +, -, *, or /"
