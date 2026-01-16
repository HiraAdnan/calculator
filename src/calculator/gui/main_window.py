"""
Main calculator window.

Integrates display, button grid, and calculator logic.
"""

from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from PyQt6.QtCore import Qt
from calculator.gui.display import CalculatorDisplay
from calculator.gui.button_grid import ButtonGrid
from calculator.gui.calculator_logic import CalculatorState
from calculator.gui.styles import WINDOW_STYLE


class CalculatorWindow(QMainWindow):
    """
    Main calculator application window.

    Integrates display, button grid, and calculator logic.
    """

    def __init__(self) -> None:
        """Initialize the calculator window."""
        super().__init__()
        self._state = CalculatorState()
        self._setup_ui()
        self._connect_signals()

    def _setup_ui(self) -> None:
        """Create and arrange UI components."""
        self.setWindowTitle("Calculator")
        self.setFixedSize(320, 480)
        self.setStyleSheet(WINDOW_STYLE)

        central = QWidget()
        self.setCentralWidget(central)

        layout = QVBoxLayout(central)
        layout.setSpacing(8)
        layout.setContentsMargins(8, 8, 8, 8)

        self._display = CalculatorDisplay()
        layout.addWidget(self._display)

        self._buttons = ButtonGrid()
        layout.addWidget(self._buttons, stretch=1)

    def _connect_signals(self) -> None:
        """Connect button signals to calculator logic."""
        self._buttons.digit_clicked.connect(self._on_digit)
        self._buttons.operation_clicked.connect(self._on_operation)
        self._buttons.equals_clicked.connect(self._on_equals)
        self._buttons.clear_clicked.connect(self._on_clear)
        self._buttons.decimal_clicked.connect(self._on_decimal)
        self._buttons.negate_clicked.connect(self._on_negate)
        self._buttons.backspace_clicked.connect(self._on_backspace)

    def _on_digit(self, digit: str) -> None:
        """Handle digit button press."""
        value = self._state.digit_pressed(digit)
        self._display.set_value(value)

    def _on_operation(self, op: str) -> None:
        """Handle operation button press."""
        value = self._state.operation_pressed(op)
        if value.startswith("Cannot") or value.startswith("Invalid"):
            self._display.show_error(value)
        else:
            self._display.set_value(value)

    def _on_equals(self) -> None:
        """Handle equals button press."""
        value = self._state.equals_pressed()
        if value.startswith("Cannot") or value.startswith("Invalid"):
            self._display.show_error(value)
        else:
            self._display.set_value(value)

    def _on_clear(self) -> None:
        """Handle clear button press."""
        value = self._state.clear_pressed()
        self._display.set_value(value)

    def _on_decimal(self) -> None:
        """Handle decimal button press."""
        value = self._state.decimal_pressed()
        self._display.set_value(value)

    def _on_negate(self) -> None:
        """Handle negate button press."""
        value = self._state.negate_pressed()
        self._display.set_value(value)

    def _on_backspace(self) -> None:
        """Handle backspace button press."""
        value = self._state.backspace_pressed()
        self._display.set_value(value)

    def keyPressEvent(self, event: object) -> None:
        """Handle keyboard input."""
        from PyQt6.QtGui import QKeyEvent
        if not isinstance(event, QKeyEvent):
            return

        key = event.key()
        text = event.text()

        if text.isdigit():
            self._on_digit(text)
        elif text == ".":
            self._on_decimal()
        elif text in "+-*/":
            self._on_operation(text)
        elif key in (Qt.Key.Key_Return, Qt.Key.Key_Enter, Qt.Key.Key_Equal):
            self._on_equals()
        elif key == Qt.Key.Key_Escape:
            self._on_clear()
        elif key == Qt.Key.Key_Backspace:
            self._on_backspace()
        else:
            super().keyPressEvent(event)  # type: ignore[arg-type]
