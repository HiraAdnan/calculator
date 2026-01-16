"""
Calculator GUI package - PyQt6 graphical interface.

Provides:
- CalculatorWindow: Main application window
- main: Entry point function
"""

from calculator.gui.main_window import CalculatorWindow
from calculator.gui.__main__ import main

__all__ = ["CalculatorWindow", "main"]
