# CLI Interface Contract: Calculator

**Feature**: 001-cli-calculator
**Date**: 2026-01-15

## Overview

This document defines the command-line interface contract for the calculator application. Since this is a CLI tool (not an API), the contract defines user interactions rather than HTTP endpoints.

## Entry Point

```bash
# Run the calculator
python -m calculator

# Or if installed via pip
calculator
```

## Interactive Session Contract

### Session Start

**Output**:
```
Simple Calculator
Type 'quit' or 'exit' to close

```

### Calculation Flow

#### Prompt 1: First Number

**Output**:
```
Enter first number:
```

**Valid Input**: Any numeric string (integer, decimal, negative)
- Examples: `5`, `-5`, `3.14`, `-3.14`, `0.5`

**Invalid Input Response**:
```
Error: Invalid input - please enter a number
Enter first number:
```

#### Prompt 2: Operation

**Output**:
```
Enter operation (+, -, *, /):
```

**Valid Input**: One of `+`, `-`, `*`, `/`

**Invalid Input Response**:
```
Error: Invalid operation - use +, -, *, or /
Enter operation (+, -, *, /):
```

#### Prompt 3: Second Number

**Output**:
```
Enter second number:
```

**Valid Input**: Same as first number

**Invalid Input Response**: Same as first number

### Result Display

#### Success

**Format**:
```
Result: {value}

```

**Examples**:
```
Result: 8
Result: 2.5
Result: 3.3333333333
Result: -5
```

#### Error (Division by Zero)

**Format**:
```
Error: Cannot divide by zero

```

### Session Loop

After displaying result, return to Prompt 1 for next calculation.

### Session Exit

**Trigger**: User enters `quit` or `exit` at any prompt

**Output**:
```
Goodbye!
```

**Exit Code**: `0`

## Input Validation Contract

| Input Type | Valid Pattern | Error Message |
|------------|---------------|---------------|
| Number | `^-?\d+\.?\d*$` | `Error: Invalid input - please enter a number` |
| Operation | `^[+\-*/]$` | `Error: Invalid operation - use +, -, *, or /` |
| Empty | `^\s*$` | `Error: Please enter a value` |

## Output Format Contract

| Scenario | Format | Example |
|----------|--------|---------|
| Integer result | No decimal | `8` |
| Decimal result (clean) | Minimal decimals | `2.5` |
| Decimal result (long) | Up to 10 decimals | `3.3333333333` |
| Negative result | Leading minus | `-5` |
| Error | `Error: {message}` | `Error: Cannot divide by zero` |

## Full Session Example

```
Simple Calculator
Type 'quit' or 'exit' to close

Enter first number: 10
Enter operation (+, -, *, /): /
Enter second number: 4
Result: 2.5

Enter first number: 5
Enter operation (+, -, *, /): +
Enter second number: abc
Error: Invalid input - please enter a number
Enter second number: 3
Result: 8

Enter first number: 10
Enter operation (+, -, *, /): /
Enter second number: 0
Error: Cannot divide by zero

Enter first number: quit
Goodbye!
```

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Normal exit (user typed quit/exit) |
| 1 | Unexpected error (should never happen) |
