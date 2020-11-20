import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor


class Circless(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.draw = False
        self.show()

    def paintEvent(self, event):
        if not self.draw:
            return
        qp = QPainter()
        qp.begin(self)
        self.drawCircles(qp)
        qp.end()

    def run(self):
        self.draw = True
        self.update()

    def drawCircles(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        x = random.randint(1, self.width())
        y = random.randint(50, self.height())
        w = random.randint(10, 100)
        qp.drawEllipse(x, y, w, w)


app = QApplication(sys.argv)
ex = Circless()
sys.exit(app.exec_())
