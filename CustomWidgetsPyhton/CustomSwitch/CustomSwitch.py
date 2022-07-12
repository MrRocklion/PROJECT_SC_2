from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class CSwitch(QCheckBox):
    def __init__(
            self,
            width = 60 ,
            bg_color = "#777",
            circle_color = "#DDD",
            active_color = "#00BCFF",
            animation_curve = QEasingCurve.OutQuint
        ):
        QCheckBox.__init__(self)
        self.setFixedSize(width, 28)
        self.setCursor(Qt.PointingHandCursor)

        #colores

        self._bg_color = bg_color
        self._circle_color = circle_color
        self._active_color = active_color
        #animation
        self._circle_position = 3
        self.animation = QPropertyAnimation(self,b"circle_position",self)
        self.animation.setEasingCurve(animation_curve)
        self.animation.setDuration(500)
        #una vez que cambia el estado
        self.stateChanged.connect(self.start_transition)
    @Property(float)
    def circle_position(self):
        return self._circle_position
    @circle_position.setter
    def circle_position(self,pos):
        self._circle_position = pos
        self.update()
    def start_transition(self,value):
        self.animation.stop()
        if value:
            self.animation.setEndValue(self.width()-26)
        else:
            self.animation.setEndValue(3)
        self.animation.start()
    def debug(self):
        print(f"Status:{self.isChecked()}")
    def hitButton(self, pos: QPoint):
        return self.contentsRect().contains(pos)
    def paintEvent(self, arg__1):
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)
        p.setPen(Qt.NoPen)
        rect = QRect(0,0,self.width(),self.height())



        if not self.isChecked():
            p.setBrush(QColor(self._bg_color))
            p.drawRoundedRect(0, 0, rect.width(), rect.height(), self.height() / 2, self.height() / 2)
            p.setBrush(QColor(self._circle_color))
            p.drawEllipse(self._circle_position,3,22,22)
        else:
            p.setBrush(QColor(self._active_color))
            p.drawRoundedRect(0, 0, rect.width(), rect.height(), self.height() / 2, self.height() / 2)
            p.setBrush(QColor(self._circle_color))
            p.drawEllipse(self._circle_position,self.height()-26,22,22)

        p.end()