# QA Test Strategy for Rochambeau (Rock-Paper-Scissors)

## 1. Test Categories

### A. Unit Tests
- Test all core functions: `determine_winner`, `get_ascii_art`, `get_computer_choice`, `get_player_choice` (mocked input).
- Test input validation and output formatting.

### B. Integration Tests
- Simulate full game flow with various user input sequences (mock input/output).
- Test scorekeeping and round progression.

### C. Edge Case Tests
- Invalid inputs (empty, whitespace, special characters, numbers outside valid range, mixed case, etc.).
- Rapid exit (user exits immediately).
- Long play sessions (many rounds).
- All possible win/loss/tie combinations.
- Terminal/console compatibility (Windows, Linux, macOS).

### D. Usability Tests
- Verify clear prompts and error messages.
- Check ASCII art alignment and animation.
- Color output visibility (if supported).

## 2. Edge Cases
- User enters only whitespace or presses Enter.
- User enters mixed-case input (e.g., "RoCk").
- User enters invalid input multiple times before a valid one.
- User enters exit command in various forms (e.g., "4", "q", "exit", "E").
- Computer and player always tie.
- Player always wins or always loses.
- User plays all valid input types (full word, letter, number).

## 3. Pass/Fail Criteria
- All valid inputs are accepted and mapped correctly.
- All invalid inputs are rejected with a clear error message.
- Game flow proceeds as expected for all input sequences.
- Scoreboard updates correctly after each round.
- ASCII art and color output display correctly.
- Game exits gracefully on any valid exit command.
- All tests pass in automated test suite (unit and integration).

## 4. Automation
- Use `unittest` and `unittest.mock` for automated testing.
- Run tests on every code change (locally and in CI).
- Review test coverage and add tests for uncovered code paths.

---

# Example Test Summary Output
- Each test prints a friendly summary of what was tested and the result (pass/fail).
- At the end, print a total summary of all tests.

---
