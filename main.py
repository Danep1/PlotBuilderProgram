from sys import exit, argv
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
import modern_func
import build_graf



class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main_uiui.ui', self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        pass


app = QApplication(argv)
ex = MyWidget()
ex.show()
exit(app.exec_())
