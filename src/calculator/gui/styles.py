"""
QSS Stylesheets for calculator GUI.

Provides dark theme styling for a modern calculator appearance.
"""

COLORS = {
    "background": "#1C1C1E",
    "display_bg": "#000000",
    "display_text": "#FFFFFF",
    "digit_bg": "#505050",
    "digit_hover": "#6B6B6B",
    "digit_pressed": "#404040",
    "operation_bg": "#FF9500",
    "operation_hover": "#FFB143",
    "operation_pressed": "#CC7700",
    "equals_bg": "#FF9500",
    "clear_bg": "#A5A5A5",
    "clear_hover": "#B8B8B8",
    "function_bg": "#636366",
    "function_hover": "#7C7C80",
}

WINDOW_STYLE = f"""
    QMainWindow {{
        background-color: {COLORS["background"]};
    }}
    QWidget {{
        background-color: {COLORS["background"]};
    }}
"""

DISPLAY_STYLE = f"""
    QLineEdit {{
        background-color: {COLORS["display_bg"]};
        color: {COLORS["display_text"]};
        border: none;
        font-size: 48px;
        font-weight: 300;
        padding: 10px 15px;
        qproperty-alignment: AlignRight;
    }}
"""

DIGIT_BUTTON_STYLE = f"""
    QPushButton {{
        background-color: {COLORS["digit_bg"]};
        color: white;
        border: none;
        border-radius: 10px;
        font-size: 24px;
        font-weight: 500;
    }}
    QPushButton:hover {{
        background-color: {COLORS["digit_hover"]};
    }}
    QPushButton:pressed {{
        background-color: {COLORS["digit_pressed"]};
    }}
"""

OPERATION_BUTTON_STYLE = f"""
    QPushButton {{
        background-color: {COLORS["operation_bg"]};
        color: white;
        border: none;
        border-radius: 10px;
        font-size: 28px;
        font-weight: 500;
    }}
    QPushButton:hover {{
        background-color: {COLORS["operation_hover"]};
    }}
    QPushButton:pressed {{
        background-color: {COLORS["operation_pressed"]};
    }}
"""

FUNCTION_BUTTON_STYLE = f"""
    QPushButton {{
        background-color: {COLORS["function_bg"]};
        color: white;
        border: none;
        border-radius: 10px;
        font-size: 20px;
        font-weight: 500;
    }}
    QPushButton:hover {{
        background-color: {COLORS["function_hover"]};
    }}
    QPushButton:pressed {{
        background-color: {COLORS["digit_pressed"]};
    }}
"""

CLEAR_BUTTON_STYLE = f"""
    QPushButton {{
        background-color: {COLORS["clear_bg"]};
        color: black;
        border: none;
        border-radius: 10px;
        font-size: 20px;
        font-weight: 500;
    }}
    QPushButton:hover {{
        background-color: {COLORS["clear_hover"]};
    }}
    QPushButton:pressed {{
        background-color: {COLORS["digit_hover"]};
    }}
"""


def get_button_style(button_type: str) -> str:
    """
    Return appropriate stylesheet for button type.

    Args:
        button_type: One of 'digit', 'operation', 'function', 'clear'

    Returns:
        QSS stylesheet string
    """
    styles = {
        "digit": DIGIT_BUTTON_STYLE,
        "operation": OPERATION_BUTTON_STYLE,
        "function": FUNCTION_BUTTON_STYLE,
        "clear": CLEAR_BUTTON_STYLE,
    }
    return styles.get(button_type, DIGIT_BUTTON_STYLE)
