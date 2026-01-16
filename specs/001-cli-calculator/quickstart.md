# Quickstart: CLI Calculator

**Feature**: 001-cli-calculator
**Date**: 2026-01-15

## Prerequisites

- Python 3.10 or higher
- pip (Python package manager)

## Installation

### From Source

```bash
# Clone or navigate to repository
cd path/to/calculator

# Install in development mode
pip install -e .

# Or install dependencies only
pip install -r requirements.txt
```

### Verify Installation

```bash
# Check Python version
python --version  # Should be 3.10+

# Run tests
pytest
```

## Usage

### Start the Calculator

```bash
# Run as module
python -m calculator

# Or if installed
calculator
```

### Perform Calculations

The calculator prompts for input step-by-step:

```
Simple Calculator
Type 'quit' or 'exit' to close

Enter first number: 10
Enter operation (+, -, *, /): +
Enter second number: 5
Result: 15

Enter first number:
```

### Supported Operations

| Operation | Symbol | Example |
|-----------|--------|---------|
| Addition | `+` | `5 + 3 = 8` |
| Subtraction | `-` | `10 - 4 = 6` |
| Multiplication | `*` | `4 * 3 = 12` |
| Division | `/` | `10 / 4 = 2.5` |

### Number Formats

The calculator accepts:

- Integers: `5`, `100`, `0`
- Decimals: `3.14`, `0.5`, `2.0`
- Negative numbers: `-5`, `-3.14`

### Exit

Type `quit` or `exit` at any prompt to close the calculator.

## Examples

### Basic Calculation

```
Enter first number: 25
Enter operation (+, -, *, /): *
Enter second number: 4
Result: 100
```

### Decimal Numbers

```
Enter first number: 3.14
Enter operation (+, -, *, /): *
Enter second number: 2
Result: 6.28
```

### Negative Numbers

```
Enter first number: -10
Enter operation (+, -, *, /): +
Enter second number: 3
Result: -7
```

### Division with Decimal Result

```
Enter first number: 10
Enter operation (+, -, *, /): /
Enter second number: 3
Result: 3.3333333333
```

### Error: Division by Zero

```
Enter first number: 10
Enter operation (+, -, *, /): /
Enter second number: 0
Error: Cannot divide by zero
```

### Error: Invalid Input

```
Enter first number: abc
Error: Invalid input - please enter a number
Enter first number: 5
```

## Development

### Run Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=calculator

# Run specific test file
pytest tests/test_operations.py
```

### Type Checking

```bash
# Run mypy
mypy src/calculator --strict
```

### Project Structure

```
src/calculator/
├── __init__.py      # Package init
├── operations.py    # Math operations
├── parser.py        # Input validation
└── cli.py           # User interface

tests/
├── test_operations.py
├── test_parser.py
└── test_cli.py
```

## Troubleshooting

### "python: command not found"

Ensure Python 3.10+ is installed and in your PATH:
```bash
python3 --version
# Use python3 instead of python if needed
```

### "ModuleNotFoundError: calculator"

Install the package first:
```bash
pip install -e .
```

### Tests Failing

Ensure you're using Python 3.10+:
```bash
python --version
```
