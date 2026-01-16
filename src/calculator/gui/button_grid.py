"""
Calculator button grid widget.

Provides the button layout for the calculator interface.
"""

from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy
from PyQt6.QtCore import pyqtSignal
from calculator.gui.styles import get_button_style


class CalculatorButton(QPushButton):
    """
    Styled calculator button.

    Args:
        text: Button label
        button_type: 'digit', 'operation', 'function', or 'clear'
    """

    def __init__(
        self,
        text: str,
        button_type: str = "digit",
        parent: QWidget | None = None
    ) -> None:
        """
        Initialize the calculator button.

        Args:
            text: Button label
            button_type: Type for styling
            parent: Parent widget
        """
        super().__init__(text, parent)
        self.setMinimumSize(60, 60)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.setStyleSheet(get_button_style(button_type))


class ButtonGrid(QWidget):
    """
    Grid layout of calculator buttons.

    Emits signals for button presses that the main window can connect to.
    """

    digit_clicked = pyqtSignal(str)
    operation_clicked = pyqtSignal(str)
    equals_clicked = pyqtSignal()
    clear_clicked = pyqtSignal()
    decimal_clicked = pyqtSignal()
    negate_clicked = pyqtSignal()
    backspace_clicked = pyqtSignal()

    def __init__(self, parent: QWidget | None = None) -> None:
        """
        Initialize the button grid.

        Args:
            parent: Parent widget
        """
        super().__init__(parent)
        self._layout = QGridLayout(self)
        self._layout.setSpacing(10)
        self._layout.setContentsMargins(5, 5, 5, 5)
        self._create_buttons()

    def _create_buttons(self) -> None:
        """Create and arrange all buttons in grid."""
        # Row 0: C, +/-, <-, /
        self._add_button("C", 0, 0, "clear", self.clear_clicked.emit)
        self._add_button("+/-", 0, 1, "function", self.negate_clicked.emit)
        self._add_button("<-", 0, 2, "function", self.backspace_clicked.emit)
        self._add_button("/", 0, 3, "operation", lambda: self.operation_clicked.emit("/"))

        # Row 1: 7, 8, 9, *
        self._add_button("7", 1, 0, "digit", lambda: self.digit_clicked.emit("7"))
        self._add_button("8", 1, 1, "digit", lambda: self.digit_clicked.emit("8"))
        self._add_button("9", 1, 2, "digit", lambda: self.digit_clicked.emit("9"))
        self._add_button("*", 1, 3, "operation", lambda: self.operation_clicked.emit("*"))

        # Row 2: 4, 5, 6, -
        self._add_button("4", 2, 0, "digit", lambda: self.digit_clicked.emit("4"))
        self._add_button("5", 2, 1, "digit", lambda: self.digit_clicked.emit("5"))
        self._add_button("6", 2, 2, "digit", lambda: self.digit_clicked.emit("6"))
        self._add_button("-", 2, 3, "operation", lambda: self.operation_clicked.emit("-"))

        # Row 3: 1, 2, 3, +
        self._add_button("1", 3, 0, "digit", lambda: self.digit_clicked.emit("1"))
        self._add_button("2", 3, 1, "digit", lambda: self.digit_clicked.emit("2"))
        self._add_button("3", 3, 2, "digit", lambda: self.digit_clicked.emit("3"))
        self._add_button("+", 3, 3, "operation", lambda: self.operation_clicked.emit("+"))

        # Row 4: 0 (spans 2 cols), ., =
        zero_btn = CalculatorButton("0", "digit")
        zero_btn.clicked.connect(lambda: self.digit_clicked.emit("0"))
        self._layout.addWidget(zero_btn, 4, 0, 1, 2)

        self._add_button(".", 4, 2, "digit", self.decimal_clicked.emit)
        self._add_button("=", 4, 3, "operation", self.equals_clicked.emit)

    def _add_button(
        self,
        text: str,
        row: int,
        col: int,
        button_type: str,
        callback: object
    ) -> None:
        """
        Create a button and add it to the grid.

        Args:
            text: Button label
            row: Grid row
            col: Grid column
            button_type: Type for styling
            callback: Function to call on click
        """
        button = CalculatorButton(text, button_type)
        button.clicked.connect(callback)  # type: ignore[arg-type]
        self._layout.addWidget(button, row, col)
