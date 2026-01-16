"""Entry point for running calculator GUI: python -m calculator.gui"""

import sys
from PyQt6.QtWidgets import QApplication
from calculator.gui.main_window import CalculatorWindow


def main() -> None:
    """Launch the calculator GUI application."""
    app = QApplication(sys.argv)
    app.setApplicationName("Calculator")

    window = CalculatorWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
