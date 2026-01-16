# Tasks: CLI Calculator

**Input**: Design documents from `/specs/001-cli-calculator/`
**Prerequisites**: plan.md (required), spec.md (required), research.md, data-model.md, contracts/

**Tests**: Included per Constitution Principle III (Test-First Development)

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3, US4)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/calculator/`, `tests/` at repository root
- Paths based on plan.md structure

---

## Phase 1: Setup

**Purpose**: Project initialization and basic structure

- [x] T001 Create project directory structure: `src/calculator/`, `tests/`
- [x] T002 Create `pyproject.toml` with project metadata, Python 3.10+ requirement, and pytest dependency
- [x] T003 [P] Create `src/calculator/__init__.py` with version string
- [x] T004 [P] Create `tests/__init__.py`

**Checkpoint**: Project structure ready, pytest can be invoked (no tests yet)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**CRITICAL**: No user story work can begin until this phase is complete

- [x] T005 [P] Create empty `src/calculator/operations.py` with module docstring
- [x] T006 [P] Create empty `src/calculator/parser.py` with module docstring
- [x] T007 [P] Create empty `src/calculator/cli.py` with module docstring
- [x] T008 [P] Create empty `tests/test_operations.py` with imports
- [x] T009 [P] Create empty `tests/test_parser.py` with imports
- [x] T010 [P] Create empty `tests/test_cli.py` with imports

**Checkpoint**: Foundation ready - all modules exist, user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Basic Arithmetic Operations (Priority: P1)

**Goal**: Perform add, subtract, multiply, divide operations on two integer numbers

**Independent Test**: Enter two whole numbers and an operation, verify correct result

### Tests for User Story 1

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T011 [P] [US1] Write test `test_add_integers` in `tests/test_operations.py`: assert add(5, 3) == 8
- [x] T012 [P] [US1] Write test `test_subtract_integers` in `tests/test_operations.py`: assert subtract(10, 4) == 6
- [x] T013 [P] [US1] Write test `test_multiply_integers` in `tests/test_operations.py`: assert multiply(5, 3) == 15
- [x] T014 [P] [US1] Write test `test_divide_integers` in `tests/test_operations.py`: assert divide(10, 2) == 5.0
- [x] T015 [P] [US1] Write test `test_calculate_dispatch` in `tests/test_operations.py`: test calculate() routes to correct operation

### Implementation for User Story 1

- [x] T016 [P] [US1] Implement `add(a: float, b: float) -> float` in `src/calculator/operations.py`
- [x] T017 [P] [US1] Implement `subtract(a: float, b: float) -> float` in `src/calculator/operations.py`
- [x] T018 [P] [US1] Implement `multiply(a: float, b: float) -> float` in `src/calculator/operations.py`
- [x] T019 [P] [US1] Implement `divide(a: float, b: float) -> float | str` in `src/calculator/operations.py`
- [x] T020 [US1] Implement `calculate(a: float, op: str, b: float) -> float | str` in `src/calculator/operations.py`
- [x] T021 [US1] Run pytest and verify all US1 tests pass

**Checkpoint**: User Story 1 complete - basic integer arithmetic works

---

## Phase 4: User Story 2 - Decimal Number Support (Priority: P2)

**Goal**: Accept and process decimal numbers (3.14, 0.5, etc.)

**Independent Test**: Enter decimal numbers and verify accurate results

### Tests for User Story 2

- [x] T022 [P] [US2] Write test `test_parse_decimal` in `tests/test_parser.py`: assert parse_number("3.14") == 3.14
- [x] T023 [P] [US2] Write test `test_add_decimals` in `tests/test_operations.py`: assert add(3.14, 2.5) == 5.64
- [x] T024 [P] [US2] Write test `test_divide_decimal_result` in `tests/test_operations.py`: assert divide(10, 4) == 2.5
- [x] T025 [P] [US2] Write test `test_format_decimal_result` in `tests/test_cli.py`: assert format_result(2.5) == "2.5"
- [x] T026 [P] [US2] Write test `test_format_strips_trailing_zeros` in `tests/test_cli.py`: assert format_result(8.0) == "8"

### Implementation for User Story 2

- [x] T027 [US2] Implement `parse_number(value: str) -> float | str` in `src/calculator/parser.py` (handles decimals)
- [x] T028 [US2] Implement `format_result(value: float) -> str` in `src/calculator/cli.py` (strips trailing zeros)
- [x] T029 [US2] Run pytest and verify all US2 tests pass

**Checkpoint**: User Story 2 complete - decimal numbers work correctly

---

## Phase 5: User Story 3 - Negative Number Support (Priority: P3)

**Goal**: Accept and process negative numbers (-5, -3.14, etc.)

**Independent Test**: Enter negative numbers and verify correct mathematical results

### Tests for User Story 3

- [x] T030 [P] [US3] Write test `test_parse_negative` in `tests/test_parser.py`: assert parse_number("-5") == -5.0
- [x] T031 [P] [US3] Write test `test_parse_negative_decimal` in `tests/test_parser.py`: assert parse_number("-3.14") == -3.14
- [x] T032 [P] [US3] Write test `test_add_negative` in `tests/test_operations.py`: assert add(-5, 3) == -2
- [x] T033 [P] [US3] Write test `test_multiply_negatives` in `tests/test_operations.py`: assert multiply(-5, -3) == 15
- [x] T034 [P] [US3] Write test `test_divide_negative` in `tests/test_operations.py`: assert divide(-10, 2) == -5.0

### Implementation for User Story 3

- [x] T035 [US3] Update `parse_number()` in `src/calculator/parser.py` to handle negative numbers (likely already works via float())
- [x] T036 [US3] Run pytest and verify all US3 tests pass

**Checkpoint**: User Story 3 complete - negative numbers work correctly

---

## Phase 6: User Story 4 - Error Handling (Priority: P4)

**Goal**: Display clear error messages for invalid input and division by zero

**Independent Test**: Enter invalid inputs and verify appropriate error messages

### Tests for User Story 4

- [x] T037 [P] [US4] Write test `test_divide_by_zero` in `tests/test_operations.py`: assert divide(5, 0) returns error string
- [x] T038 [P] [US4] Write test `test_parse_invalid_input` in `tests/test_parser.py`: assert parse_number("abc") returns error string
- [x] T039 [P] [US4] Write test `test_parse_empty_input` in `tests/test_parser.py`: assert parse_number("") returns error string
- [x] T040 [P] [US4] Write test `test_parse_invalid_operation` in `tests/test_parser.py`: assert parse_operation("%") returns error string
- [x] T041 [P] [US4] Write test `test_calculate_invalid_operation` in `tests/test_operations.py`: assert calculate(5, "%", 3) returns error string

### Implementation for User Story 4

- [x] T042 [US4] Update `divide()` in `src/calculator/operations.py` to check for zero divisor and return error string
- [x] T043 [US4] Update `parse_number()` in `src/calculator/parser.py` to return error string for invalid input
- [x] T044 [US4] Implement `parse_operation(value: str) -> str` in `src/calculator/parser.py` with validation
- [x] T045 [US4] Update `calculate()` in `src/calculator/operations.py` to handle invalid operation
- [x] T046 [US4] Run pytest and verify all US4 tests pass

**Checkpoint**: User Story 4 complete - all error cases handled gracefully

---

## Phase 7: CLI Integration

**Purpose**: Connect all components into working CLI application

### Tests for CLI Integration

- [x] T047 [P] Write test `test_is_exit_command` in `tests/test_cli.py`: assert is_exit_command("quit") == True
- [x] T048 [P] Write test `test_is_exit_command_case_insensitive` in `tests/test_cli.py`: assert is_exit_command("QUIT") == True

### Implementation for CLI

- [x] T049 Implement `is_exit_command(value: str) -> bool` in `src/calculator/cli.py`
- [x] T050 Implement `main()` function in `src/calculator/cli.py` with interactive loop
- [x] T051 Add `__main__.py` entry point in `src/calculator/__main__.py`
- [x] T052 Update `pyproject.toml` with console script entry point
- [x] T053 Run full test suite and verify all tests pass

**Checkpoint**: Full CLI application working

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Final validation and documentation

- [x] T054 [P] Run mypy type checking: `mypy src/calculator --strict`
- [x] T055 [P] Verify all module docstrings are present
- [x] T056 Run quickstart.md validation - test all documented examples
- [x] T057 Final integration test - run calculator manually and verify all user stories

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-6)**: All depend on Foundational phase completion
  - US1, US2, US3, US4 can proceed in priority order (P1 → P2 → P3 → P4)
  - OR in parallel if multiple developers available
- **CLI Integration (Phase 7)**: Depends on all user stories complete
- **Polish (Phase 8)**: Depends on CLI Integration complete

### User Story Dependencies

- **User Story 1 (P1)**: No dependencies on other stories - MVP standalone
- **User Story 2 (P2)**: Independent - decimal parsing extends US1 naturally
- **User Story 3 (P3)**: Independent - negative numbers extend parsing
- **User Story 4 (P4)**: Independent - error handling is orthogonal to other stories

### Within Each User Story

- Tests MUST be written and FAIL before implementation
- Implementation makes tests pass
- Story complete when all story tests pass

### Parallel Opportunities

- All Setup tasks (T001-T004) can run in parallel after T001
- All Foundational tasks (T005-T010) can run in parallel
- All test tasks within a user story can run in parallel
- Implementation tasks within story depend on their tests

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together:
Task: T011 "Write test_add_integers"
Task: T012 "Write test_subtract_integers"
Task: T013 "Write test_multiply_integers"
Task: T014 "Write test_divide_integers"
Task: T015 "Write test_calculate_dispatch"

# After tests written, launch parallel implementations:
Task: T016 "Implement add()"
Task: T017 "Implement subtract()"
Task: T018 "Implement multiply()"
Task: T019 "Implement divide()"

# Then sequentially:
Task: T020 "Implement calculate()" (depends on T016-T019)
Task: T021 "Run pytest" (depends on all above)
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Calculator works with integers
5. Can demo basic add/subtract/multiply/divide

### Incremental Delivery

1. Setup + Foundational → Project ready
2. Add User Story 1 → MVP with integer arithmetic
3. Add User Story 2 → Now supports decimals
4. Add User Story 3 → Now supports negative numbers
5. Add User Story 4 → Now handles all errors gracefully
6. Add CLI Integration → Complete application
7. Polish → Production ready

### Sequential Solo Developer

Execute phases in order: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8

Each user story is independently testable checkpoint.

---

## Summary

| Phase | Tasks | Story | Parallel Tasks |
|-------|-------|-------|----------------|
| 1. Setup | T001-T004 | - | 2 |
| 2. Foundational | T005-T010 | - | 6 |
| 3. User Story 1 | T011-T021 | US1 | 9 |
| 4. User Story 2 | T022-T029 | US2 | 5 |
| 5. User Story 3 | T030-T036 | US3 | 5 |
| 6. User Story 4 | T037-T046 | US4 | 5 |
| 7. CLI Integration | T047-T053 | - | 2 |
| 8. Polish | T054-T057 | - | 2 |

**Total Tasks**: 57
**Parallelizable**: 36 (63%)

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story is independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
