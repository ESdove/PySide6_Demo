import sys

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QErrorMessage-Debug")
        self.resize(500, 500)
        # self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        QErrorMessage.qtHandler()
        # qDebug("XXX")
        qWarning("123")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    # window.show()

    sys.exit(app.exec_())
