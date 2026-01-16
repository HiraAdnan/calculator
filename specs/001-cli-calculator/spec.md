# Feature Specification: CLI Calculator

**Feature Branch**: `001-cli-calculator`
**Created**: 2026-01-15
**Status**: Draft
**Input**: User description: "Build a basic CLI based calculator that handles addition, subtraction, multiplication and division with challenges: decimal handling, division with zero, handle negative numbers, invalid input (e.g alphabets)"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Basic Arithmetic Operations (Priority: P1)

As a user, I want to perform basic arithmetic operations (addition, subtraction, multiplication, division) through a command-line interface so that I can quickly calculate results without opening a graphical application.

**Why this priority**: Core calculator functionality - without this, the calculator has no value. This is the MVP that delivers the primary user need.

**Independent Test**: Can be fully tested by entering two numbers and an operation, verifying the correct result is displayed.

**Acceptance Scenarios**:

1. **Given** the calculator is running, **When** I enter two numbers and select addition, **Then** the sum of the two numbers is displayed
2. **Given** the calculator is running, **When** I enter two numbers and select subtraction, **Then** the difference is displayed
3. **Given** the calculator is running, **When** I enter two numbers and select multiplication, **Then** the product is displayed
4. **Given** the calculator is running, **When** I enter two numbers and select division, **Then** the quotient is displayed

---

### User Story 2 - Decimal Number Support (Priority: P2)

As a user, I want to perform calculations with decimal numbers so that I can work with precise values and fractional amounts.

**Why this priority**: Extends basic functionality to real-world use cases. Many calculations require decimal precision, but integer operations alone still provide value.

**Independent Test**: Can be fully tested by entering decimal numbers (e.g., 3.14, 0.5) and verifying accurate results.

**Acceptance Scenarios**:

1. **Given** the calculator is running, **When** I enter decimal numbers like 3.14 and 2.5 and select addition, **Then** the correct sum (5.64) is displayed
2. **Given** the calculator is running, **When** I divide 10 by 4, **Then** the result 2.5 is displayed (not truncated to 2)
3. **Given** the calculator is running, **When** I enter 0.1 and 0.2 and select addition, **Then** the result displays a reasonable precision (e.g., 0.3 or 0.30)

---

### User Story 3 - Negative Number Support (Priority: P3)

As a user, I want to perform calculations with negative numbers so that I can handle debts, temperatures below zero, or other negative values.

**Why this priority**: Common real-world scenario, but positive number operations cover the majority of basic use cases.

**Independent Test**: Can be fully tested by entering negative numbers and verifying correct mathematical results.

**Acceptance Scenarios**:

1. **Given** the calculator is running, **When** I enter -5 and 3 and select addition, **Then** the result -2 is displayed
2. **Given** the calculator is running, **When** I enter -5 and -3 and select multiplication, **Then** the result 15 is displayed
3. **Given** the calculator is running, **When** I enter -10 and 2 and select division, **Then** the result -5 is displayed

---

### User Story 4 - Error Handling (Priority: P4)

As a user, I want clear error messages when I make mistakes so that I understand what went wrong and can correct my input.

**Why this priority**: Improves usability but the calculator can function without sophisticated error handling. Basic operations must work first.

**Independent Test**: Can be fully tested by deliberately entering invalid inputs and verifying appropriate error messages.

**Acceptance Scenarios**:

1. **Given** the calculator is running, **When** I attempt to divide by zero, **Then** a clear error message is displayed (e.g., "Cannot divide by zero")
2. **Given** the calculator is running, **When** I enter alphabetic characters instead of numbers, **Then** a clear error message is displayed (e.g., "Invalid input: please enter a number")
3. **Given** the calculator is running, **When** I enter an invalid operation, **Then** a clear error message is displayed listing valid operations

---

### Edge Cases

- What happens when user divides by zero? Display error message, do not crash
- What happens when user enters letters instead of numbers? Display error message prompting for valid numeric input
- What happens when user enters very large numbers? Handle within standard numeric limits; display overflow error if exceeded
- What happens when user enters empty input? Prompt user to enter a value
- What happens when decimal division results in repeating decimals (e.g., 10/3)? Display result with reasonable precision (2-6 decimal places)

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST provide addition operation that adds two numbers and displays the sum
- **FR-002**: System MUST provide subtraction operation that subtracts the second number from the first and displays the difference
- **FR-003**: System MUST provide multiplication operation that multiplies two numbers and displays the product
- **FR-004**: System MUST provide division operation that divides the first number by the second and displays the quotient
- **FR-005**: System MUST accept decimal numbers (e.g., 3.14, 0.5, -2.7) as valid input
- **FR-006**: System MUST accept negative numbers (e.g., -5, -3.14) as valid input
- **FR-007**: System MUST display an error message when user attempts to divide by zero
- **FR-008**: System MUST display an error message when user enters non-numeric input (alphabets, special characters)
- **FR-009**: System MUST operate via command-line interface accepting user input from keyboard
- **FR-010**: System MUST display calculation results to the user after each operation
- **FR-011**: System MUST handle decimal results with reasonable precision (minimum 2 decimal places when applicable)

### Key Entities

- **Number**: A numeric value that can be integer or decimal, positive or negative. Used as operands in calculations.
- **Operation**: One of four arithmetic operations (addition, subtraction, multiplication, division) selected by the user.
- **Result**: The calculated output from applying an operation to two numbers.
- **Error**: A message displayed when invalid input is detected or an impossible operation is attempted.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can complete a basic calculation (enter two numbers, select operation, view result) in under 30 seconds
- **SC-002**: 100% of valid arithmetic operations produce mathematically correct results
- **SC-003**: All four operations (add, subtract, multiply, divide) are accessible and functional
- **SC-004**: Division by zero displays a user-friendly error message instead of crashing
- **SC-005**: Invalid input (non-numeric characters) displays a helpful error message guiding user to correct input
- **SC-006**: Decimal number calculations maintain accuracy to at least 2 decimal places
- **SC-007**: Negative number calculations produce mathematically correct results

## Assumptions

- The calculator operates in single-operation mode (two operands, one operation per calculation)
- No calculation history or memory features are required
- No expression parsing is required (e.g., no support for "2+3*4" as a single input)
- Standard floating-point precision is acceptable for decimal calculations
- The calculator runs until the user explicitly exits
- Input/output is text-based via standard command-line interface
