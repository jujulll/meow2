import sys
import random

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 420, 400)

        self.btn = QPushButton(self)
        self.btn.move(180, 15)
        self.btn.resize(100, 30)
        self.btn.setText('Показать')
        self.btn.clicked.connect(self.click)

        self.flag = False

    def click(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def draw(self, qp):
        qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        a = random.randint(20, 180)
        b = random.randint(25, 180)
        f = random.randint(1, 180)
        qp.drawEllipse(a, b, f, f)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())