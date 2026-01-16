# Implementation Plan: CLI Calculator

**Branch**: `001-cli-calculator` | **Date**: 2026-01-15 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-cli-calculator/spec.md`

## Summary

Build a command-line calculator supporting four basic arithmetic operations (addition, subtraction, multiplication, division) with proper handling of decimal numbers, negative numbers, and error conditions (division by zero, invalid input). The implementation follows a simple, type-safe Python design with clear separation between input parsing, calculation logic, and output formatting.

## Technical Context

**Language/Version**: Python 3.10+ (per constitution - required for modern type syntax)
**Primary Dependencies**: None (standard library only per Simplicity principle)
**Storage**: N/A (stateless calculator, no persistence required)
**Testing**: pytest (per constitution)
**Target Platform**: Cross-platform CLI (Windows, macOS, Linux)
**Project Type**: Single project
**Performance Goals**: Instant response (<100ms for any calculation)
**Constraints**: No external dependencies; type hints required; single-operation mode
**Scale/Scope**: Single-user CLI application

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Requirement | Status | Notes |
|-----------|-------------|--------|-------|
| I. Type Safety | All functions have type hints | ✅ PASS | Will use `float` for numbers, `str` for operation |
| II. Simplicity | No unnecessary dependencies | ✅ PASS | Standard library only |
| II. Simplicity | YAGNI - only requested features | ✅ PASS | 4 operations, error handling only |
| III. Test-First | Tests before implementation | ✅ PASS | Will follow Red-Green-Refactor |
| III. Test-First | Edge cases tested | ✅ PASS | Division by zero, invalid input in scope |
| IV. Documentation | Module docstrings | ✅ PASS | Will add to each module |
| IV. Documentation | README with usage | ✅ PASS | quickstart.md covers this |
| V. Single Responsibility | Separate parsing/logic/output | ✅ PASS | Three-module design |

**Gate Status**: PASSED - No violations, proceed to design.

## Project Structure

### Documentation (this feature)

```text
specs/001-cli-calculator/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/           # Phase 1 output (CLI interface contract)
└── tasks.md             # Phase 2 output (/sp.tasks command)
```

### Source Code (repository root)

```text
src/
└── calculator/
    ├── __init__.py          # Package initialization, version
    ├── operations.py        # Pure calculation functions (add, subtract, multiply, divide)
    ├── parser.py            # Input parsing and validation
    └── cli.py               # Main entry point, user interaction loop

tests/
├── __init__.py
├── test_operations.py       # Unit tests for calculation functions
├── test_parser.py           # Unit tests for input parsing
└── test_cli.py              # Integration tests for CLI behavior

pyproject.toml               # Project metadata, dependencies, pytest config
```

**Structure Decision**: Single project layout following constitution's recommended structure. The `src/calculator/` layout enables proper packaging while keeping code organized by responsibility:
- `operations.py` - Pure math (Single Responsibility)
- `parser.py` - Input handling (Single Responsibility)
- `cli.py` - User interaction (Single Responsibility)

## Complexity Tracking

> No violations - table not required.

## Design Decisions

### D1: Number Representation

**Decision**: Use Python's built-in `float` type for all numeric operations.

**Rationale**:
- Handles both integers and decimals transparently
- Standard library, no dependencies
- Sufficient precision for basic calculator (spec requires "at least 2 decimal places")
- Simplicity principle: avoid `Decimal` unless precision issues arise

**Trade-off**: May have floating-point representation issues (0.1 + 0.2 = 0.30000000000000004), but spec accepts "reasonable precision" and this is standard calculator behavior.

### D2: Input Mode

**Decision**: Interactive loop with separate prompts for each input (number1, operation, number2).

**Rationale**:
- Simplest implementation meeting spec
- Clear validation at each step
- User can correct errors immediately
- No expression parsing required (per assumptions)

### D3: Error Handling Strategy

**Decision**: Return error messages as strings, never raise exceptions to user.

**Rationale**:
- User-friendly (spec: "clear error message")
- Calculator never crashes
- Consistent output format

### D4: Output Precision

**Decision**: Display up to 10 decimal places, strip trailing zeros.

**Rationale**:
- Clean output (5.0 displays as "5", not "5.0000000000")
- Preserves precision for repeating decimals (10/3 = 3.3333333333)
- Meets spec requirement of "minimum 2 decimal places when applicable"
