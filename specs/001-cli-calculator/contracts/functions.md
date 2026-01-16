# Function Contracts: Calculator Operations

**Feature**: 001-cli-calculator
**Date**: 2026-01-15

## Overview

This document defines the function signatures and contracts for the calculator's core operations module. These contracts guide Test-First development.

## Module: `calculator.operations`

### `add(a: float, b: float) -> float`

Adds two numbers.

**Contract**:
- Input: Two float values
- Output: Sum of inputs
- Errors: None possible

**Examples**:
| a | b | Result |
|---|---|--------|
| 5 | 3 | 8 |
| -5 | 3 | -2 |
| 3.14 | 2.86 | 6.0 |
| 0 | 0 | 0 |

---

### `subtract(a: float, b: float) -> float`

Subtracts second number from first.

**Contract**:
- Input: Two float values
- Output: `a - b`
- Errors: None possible

**Examples**:
| a | b | Result |
|---|---|--------|
| 10 | 4 | 6 |
| 5 | 8 | -3 |
| -5 | -3 | -2 |
| 0 | 5 | -5 |

---

### `multiply(a: float, b: float) -> float`

Multiplies two numbers.

**Contract**:
- Input: Two float values
- Output: Product of inputs
- Errors: None possible

**Examples**:
| a | b | Result |
|---|---|--------|
| 5 | 3 | 15 |
| -5 | 3 | -15 |
| -5 | -3 | 15 |
| 0 | 100 | 0 |

---

### `divide(a: float, b: float) -> float | str`

Divides first number by second.

**Contract**:
- Input: Two float values
- Output: `a / b` on success, error string on failure
- Errors: Division by zero returns `"Error: Cannot divide by zero"`

**Examples**:
| a | b | Result |
|---|---|--------|
| 10 | 2 | 5.0 |
| 10 | 4 | 2.5 |
| 10 | 3 | 3.333... |
| -10 | 2 | -5.0 |
| 5 | 0 | `"Error: Cannot divide by zero"` |
| 0 | 5 | 0.0 |

---

### `calculate(a: float, op: str, b: float) -> float | str`

Performs the specified operation on two numbers.

**Contract**:
- Input: Two floats and an operation string
- Output: Result of operation, or error string
- Errors: Invalid operation returns error string

**Examples**:
| a | op | b | Result |
|---|-----|---|--------|
| 5 | `"+"` | 3 | 8.0 |
| 5 | `"-"` | 3 | 2.0 |
| 5 | `"*"` | 3 | 15.0 |
| 5 | `"/"` | 2 | 2.5 |
| 5 | `"/"` | 0 | `"Error: Cannot divide by zero"` |
| 5 | `"%"` | 3 | `"Error: Invalid operation - use +, -, *, or /"` |

---

## Module: `calculator.parser`

### `parse_number(value: str) -> float | str`

Parses a string into a float.

**Contract**:
- Input: String from user input
- Output: Parsed float, or error string
- Errors: Invalid input returns error string

**Examples**:
| Input | Result |
|-------|--------|
| `"5"` | 5.0 |
| `"-5"` | -5.0 |
| `"3.14"` | 3.14 |
| `"abc"` | `"Error: Invalid input - please enter a number"` |
| `""` | `"Error: Please enter a value"` |
| `"  "` | `"Error: Please enter a value"` |
| `"5.5.5"` | `"Error: Invalid input - please enter a number"` |

---

### `parse_operation(value: str) -> str | str`

Validates an operation string.

**Contract**:
- Input: String from user input
- Output: Validated operation symbol, or error string
- Errors: Invalid operation returns error string

**Examples**:
| Input | Result |
|-------|--------|
| `"+"` | `"+"` |
| `"-"` | `"-"` |
| `"*"` | `"*"` |
| `"/"` | `"/"` |
| `"%"` | `"Error: Invalid operation - use +, -, *, or /"` |
| `"add"` | `"Error: Invalid operation - use +, -, *, or /"` |
| `""` | `"Error: Please enter a value"` |

---

## Module: `calculator.cli`

### `format_result(value: float) -> str`

Formats a numeric result for display.

**Contract**:
- Input: Float value
- Output: Formatted string with trailing zeros stripped

**Examples**:
| Input | Result |
|-------|--------|
| 8.0 | `"8"` |
| 2.5 | `"2.5"` |
| 3.3333333333 | `"3.3333333333"` |
| -5.0 | `"-5"` |
| 0.0 | `"0"` |

---

### `is_exit_command(value: str) -> bool`

Checks if input is an exit command.

**Contract**:
- Input: String from user input
- Output: True if exit command, False otherwise

**Examples**:
| Input | Result |
|-------|--------|
| `"quit"` | True |
| `"exit"` | True |
| `"QUIT"` | True |
| `"EXIT"` | True |
| `"q"` | False |
| `"5"` | False |
