"""
Calculator display widget.

Provides a styled read-only display for calculator results.
"""

from PyQt6.QtWidgets import QLineEdit, QWidget
from PyQt6.QtCore import Qt
from calculator.gui.styles import DISPLAY_STYLE


class CalculatorDisplay(QLineEdit):
    """
    Read-only display for calculator results.

    Features:
    - Right-aligned text
    - Large, clear font
    - Read-only (no cursor)
    - Dark theme styling
    """

    def __init__(self, parent: QWidget | None = None) -> None:
        """
        Initialize the calculator display.

        Args:
            parent: Parent widget
        """
        super().__init__(parent)
        self._setup_display()

    def _setup_display(self) -> None:
        """Configure display properties."""
        self.setReadOnly(True)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setText("0")
        self.setStyleSheet(DISPLAY_STYLE)
        self.setMinimumHeight(80)
        self.setMaxLength(15)

    def set_value(self, value: str) -> None:
        """
        Set display text.

        Args:
            value: Value to display
        """
        if len(value) > 12:
            try:
                num = float(value)
                value = f"{num:.6e}"
            except ValueError:
                value = value[:12]
        self.setText(value)

    def get_value(self) -> str:
        """
        Get current display text.

        Returns:
            Current display value
        """
        return self.text()

    def show_error(self, message: str) -> None:
        """
        Display error message.

        Args:
            message: Error message to display
        """
        short_message = message.replace("Error: ", "")
        self.setText(short_message[:15])
