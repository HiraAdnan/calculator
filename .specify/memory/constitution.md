<!--
Sync Impact Report
==================
- Version change: 0.0.0 → 1.0.0
- Modified principles: None (initial constitution)
- Added sections:
  - Core Principles (5 principles: Type Safety, Simplicity, Test-First, Documentation, Single Responsibility)
  - Technical Standards
  - Development Workflow
  - Governance
- Removed sections: None
- Templates requiring updates:
  - .specify/templates/plan-template.md ✅ (no changes needed - generic template)
  - .specify/templates/spec-template.md ✅ (no changes needed - generic template)
  - .specify/templates/tasks-template.md ✅ (no changes needed - generic template)
- Follow-up TODOs: None
-->

# Python Calculator Constitution

## Core Principles

### I. Type Safety

All code MUST use Python type hints for function signatures and class attributes. This includes:
- All function parameters MUST have type annotations
- All function return types MUST be annotated (use `-> None` for procedures)
- Class attributes MUST be typed using class-level annotations or `__init__` parameter types
- Use `typing` module constructs (`Optional`, `Union`, `List`, `Dict`, etc.) where appropriate
- Use modern type syntax (Python 3.10+ style `X | Y` union) when compatible with target Python version

**Rationale**: Type hints enable static analysis, improve IDE support, serve as documentation, and catch errors before runtime.

### II. Simplicity

The calculator MUST remain focused and minimal:
- Implement only explicitly requested features
- Avoid premature abstraction; three similar lines are better than a premature helper
- No external dependencies unless strictly necessary for core functionality
- Prefer standard library solutions over third-party packages
- YAGNI (You Aren't Gonna Need It) applies to all design decisions

**Rationale**: A calculator is a well-defined domain. Complexity must be justified by concrete requirements, not hypothetical future needs.

### III. Test-First Development

Testing discipline MUST be followed:
- Write tests before implementation when adding new operations or features
- All public functions MUST have corresponding unit tests
- Edge cases (division by zero, overflow, invalid input) MUST be tested
- Tests MUST be runnable via `pytest` from project root
- Red-Green-Refactor cycle: tests fail first, then pass, then optimize

**Rationale**: Calculators have deterministic behavior; test-first ensures correctness and prevents regressions.

### IV. Documentation

Code MUST be self-documenting with strategic documentation:
- Module-level docstrings explaining purpose
- Public function docstrings with parameter/return descriptions for non-obvious behavior
- Type hints serve as primary inline documentation
- README MUST include installation and usage instructions
- No excessive commenting; prefer clear naming over comments

**Rationale**: Good documentation reduces onboarding time and maintenance burden while type hints provide living documentation.

### V. Single Responsibility

Each module and function MUST have one clear purpose:
- Separate parsing/input handling from calculation logic
- Separate calculation logic from output formatting
- Each mathematical operation should be independently testable
- Avoid god modules that do everything

**Rationale**: Single responsibility enables easier testing, maintenance, and future extension without breaking existing functionality.

## Technical Standards

**Language/Version**: Python 3.10+ (required for modern type syntax support)
**Package Management**: pip with `requirements.txt` or `pyproject.toml`
**Testing Framework**: pytest
**Type Checking**: mypy (recommended for CI validation)
**Code Formatting**: Consistent style (black or similar formatter recommended)
**Linting**: pylint or ruff for code quality checks

### Project Structure

```
calculator/
├── pyproject.toml      # Project metadata and dependencies
├── src/
│   └── calculator/     # Main package
│       ├── __init__.py
│       ├── operations.py   # Mathematical operations
│       └── cli.py          # Command-line interface (if applicable)
└── tests/
    ├── __init__.py
    └── test_operations.py  # Unit tests
```

### Code Quality Gates

- All functions MUST pass mypy strict mode (`mypy --strict`)
- All tests MUST pass before merge
- No `# type: ignore` without documented justification

## Development Workflow

### Change Process

1. **Understand**: Read existing code before proposing changes
2. **Plan**: For non-trivial changes, outline approach before implementation
3. **Test First**: Write failing tests that define expected behavior
4. **Implement**: Write minimal code to pass tests
5. **Refactor**: Clean up while keeping tests green
6. **Validate**: Run full test suite and type checker

### Commit Standards

- Commits MUST be atomic (one logical change per commit)
- Commit messages MUST describe the "why" not just the "what"
- Feature branches for non-trivial changes

## Governance

This constitution defines the non-negotiable standards for the Python Calculator project.

### Amendment Process

1. Propose amendment with rationale
2. Document impact on existing code
3. Update version following semantic versioning:
   - MAJOR: Principle removal or incompatible redefinition
   - MINOR: New principle added or existing principle expanded
   - PATCH: Clarifications, wording improvements
4. Update dependent documentation if affected

### Compliance

- All code reviews MUST verify adherence to these principles
- Violations require documented justification in code comments or ADR
- Constitution takes precedence over convenience

**Version**: 1.0.0 | **Ratified**: 2026-01-15 | **Last Amended**: 2026-01-15
