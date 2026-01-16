# Data Model: CLI Calculator

**Feature**: 001-cli-calculator
**Date**: 2026-01-15

## Overview

The CLI Calculator is a stateless application with no persistent storage. This document defines the logical entities and their relationships for implementation guidance.

## Entities

### Number

Represents a numeric operand in a calculation.

| Attribute | Type | Description | Constraints |
|-----------|------|-------------|-------------|
| value | float | The numeric value | Any valid float (including negative, decimal) |

**Validation Rules**:
- Must be parseable from string input
- Must handle negative numbers (e.g., `-5`, `-3.14`)
- Must handle decimal numbers (e.g., `3.14`, `0.5`)
- Must reject non-numeric input (alphabets, special characters except `-` and `.`)

**Examples**:
- Valid: `5`, `-5`, `3.14`, `-3.14`, `0.5`, `0`, `-0`
- Invalid: `abc`, `5a`, `--5`, `5.5.5`, ` ` (empty)

---

### Operation

Represents one of four arithmetic operations.

| Attribute | Type | Description | Constraints |
|-----------|------|-------------|-------------|
| symbol | str | The operation symbol | One of: `+`, `-`, `*`, `/` |

**Validation Rules**:
- Must be exactly one of the four supported symbols
- Case-insensitive alternatives not supported (simplicity)

**Mapping**:
| Symbol | Name | Function |
|--------|------|----------|
| `+` | Addition | `a + b` |
| `-` | Subtraction | `a - b` |
| `*` | Multiplication | `a * b` |
| `/` | Division | `a / b` (error if `b == 0`) |

---

### Result

Represents the output of a calculation.

| Attribute | Type | Description | Constraints |
|-----------|------|-------------|-------------|
| value | float \| str | Numeric result or error message | Error string on invalid operation |

**Output Format**:
- Numeric results: stripped trailing zeros, up to 10 decimal precision
- Error messages: descriptive string starting with "Error:"

**Examples**:
| Input | Output |
|-------|--------|
| `5 + 3` | `8` |
| `10 / 4` | `2.5` |
| `10 / 3` | `3.3333333333` |
| `5 / 0` | `Error: Cannot divide by zero` |

---

### Error

Represents an error condition.

| Attribute | Type | Description |
|-----------|------|-------------|
| message | str | User-friendly error description |

**Error Types**:
| Error | Trigger | Message |
|-------|---------|---------|
| Division by zero | `b == 0` in division | `Error: Cannot divide by zero` |
| Invalid number | Non-numeric input | `Error: Invalid input - please enter a number` |
| Invalid operation | Unknown operation symbol | `Error: Invalid operation - use +, -, *, or /` |
| Empty input | Blank/whitespace input | `Error: Please enter a value` |

---

## Entity Relationships

```
┌─────────┐     ┌───────────┐     ┌─────────┐
│ Number  │────▶│ Operation │◀────│ Number  │
│ (a)     │     │           │     │ (b)     │
└─────────┘     └─────┬─────┘     └─────────┘
                      │
                      ▼
                ┌───────────┐
                │  Result   │
                │ (or Error)│
                └───────────┘
```

## State Transitions

The calculator is stateless - each calculation is independent. The interaction flow is:

```
[Start] → [Get Number 1] → [Get Operation] → [Get Number 2] → [Calculate] → [Display Result] → [Loop or Exit]
                │                │                  │               │
                ▼                ▼                  ▼               ▼
           [Validate]      [Validate]         [Validate]     [Handle Error]
                │                │                  │               │
                ▼                ▼                  ▼               ▼
           [Error?] ───────▶ [Retry Prompt]  ◀─────────────────────┘
```

## Type Definitions (for implementation)

```python
# Type aliases for clarity
Number = float
Operation = str  # Literal["+", "-", "*", "/"]
Result = float | str  # float for success, str for error message
```
