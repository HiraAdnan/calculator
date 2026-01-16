# Research: CLI Calculator

**Feature**: 001-cli-calculator
**Date**: 2026-01-15
**Status**: Complete

## Overview

This document captures research findings for the CLI Calculator implementation. Since the project constitution pre-defines all technical choices, research focused on confirming best practices for the chosen stack.

## Research Items

### R1: Python Float vs Decimal for Calculator Operations

**Question**: Should we use `float` or `Decimal` for numeric operations?

**Decision**: Use `float`

**Rationale**:
- Constitution Principle II (Simplicity) mandates standard library preference
- `float` is built-in, `Decimal` requires import from `decimal` module
- Spec accepts "reasonable precision" (2+ decimal places)
- Basic calculator use cases don't require arbitrary precision
- Standard calculator behavior includes floating-point representation

**Alternatives Considered**:
| Option | Pros | Cons |
|--------|------|------|
| `float` | Built-in, fast, simple | Floating-point representation issues |
| `Decimal` | Exact decimal representation | More complex, overkill for basic calculator |
| `fractions.Fraction` | Exact rational numbers | Complex output, user-unfriendly |

**Conclusion**: `float` meets requirements with simplest implementation.

---

### R2: CLI Input Strategy

**Question**: How should users input operations - single expression or step-by-step?

**Decision**: Step-by-step prompts (number1 → operation → number2)

**Rationale**:
- Spec assumption: "No expression parsing required"
- Simplest implementation
- Clear error messages at each step
- User can correct mistakes immediately

**Alternatives Considered**:
| Option | Pros | Cons |
|--------|------|------|
| Step-by-step prompts | Simple, clear errors | More user interactions |
| Single-line expression | Familiar (like `2 + 3`) | Requires parser, violates YAGNI |
| Command-line arguments | Scriptable | Not interactive, violates spec |

**Conclusion**: Step-by-step matches spec assumptions and simplicity principle.

---

### R3: Error Return Strategy

**Question**: How should errors be communicated - exceptions or return values?

**Decision**: Return error strings, never raise exceptions to user

**Rationale**:
- Spec requires "clear error message" display
- Application must never crash (spec: "do not crash")
- Consistent output format

**Implementation Pattern**:
```python
def divide(a: float, b: float) -> float | str:
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b
```

**Alternatives Considered**:
| Option | Pros | Cons |
|--------|------|------|
| Return error strings | Simple, never crashes | Union type in signature |
| Raise exceptions | Pythonic | Must catch everywhere, crash risk |
| Result type (Ok/Err) | Explicit | Over-engineering for simple calculator |

**Conclusion**: Return strings keeps implementation simple and crash-free.

---

### R4: Output Formatting

**Question**: How should results be displayed, especially for decimals?

**Decision**: Strip trailing zeros, display up to 10 decimal places

**Rationale**:
- Clean output: `5.0` displays as `5`
- Repeating decimals preserved: `10/3 = 3.3333333333`
- Meets "minimum 2 decimal places when applicable" requirement

**Implementation**:
```python
def format_result(value: float) -> str:
    # Format with up to 10 decimal places, strip trailing zeros
    return f"{value:.10f}".rstrip('0').rstrip('.')
```

**Conclusion**: Standard formatting approach, simple implementation.

---

## Summary

| Item | Decision | Justification |
|------|----------|---------------|
| Number type | `float` | Simplicity, standard library |
| Input mode | Step-by-step | Spec assumption, simple |
| Error handling | Return strings | Never crash, clear messages |
| Output format | Strip trailing zeros | Clean display |

**No NEEDS CLARIFICATION items** - all technical decisions resolved from constitution and spec.
