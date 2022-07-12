
# Modules
import os
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
style = '''
QPushButton {{
	border: none;
    display: flex;
    justify-content: center;
    color: {_color};
    height: 30px;
    width: {_width};
	border-radius: {_radius};	
	background-color: transparent;
	 border: 1px solid {_color};
}}
QPushButton:hover {{
	border: 1px solid {_bg_color_hover};
	color: {_bg_color_hover}
}}
QPushButton:pressed {{	
	background-color: {_bg_color_pressed};
}}
'''

# PY PUSH BUTTON
# ///////////////////////////////////////////////////////////////
class PyPushButton(QPushButton):
    def __init__(
        self,
        width,
        text,
        radius,
        color,
        bg_color_hover,
        bg_color_pressed,
        parent = None,
    ):
        super().__init__()

        # SET PARAMETRES
        self.setText(text)
        if parent != None:
            self.setParent(parent)
        self.setCursor(Qt.PointingHandCursor)

        # SET STYLESHEET
        custom_style = style.format(
            _color = color,
            _radius = radius,
            _bg_color_hover = bg_color_hover,
            _bg_color_pressed = bg_color_pressed,
            _width = width
        )
        self.setStyleSheet(custom_style)
