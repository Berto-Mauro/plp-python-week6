```markdown
# Week 6 Assignment - Error Handling in Python

This assignment demonstrates how Python can handle errors using try and except.

## Files

- `safe_tools.py` - Contains three safe functions for division, number conversion, and dictionary field lookup.
- `unbreakable.py` - Demonstrates how a program can handle invalid input and continue running.
- `README.md` - Describes the assignment and the purpose of each file.

## Why can the if check not catch "abc" on its own?

An `if` statement can check a condition, but converting `"abc"` to an integer causes Python to raise a `ValueError` before the program can continue normally. The `try` and `except` structure is needed to catch this error and handle it without crashing the program.
```
