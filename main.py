# This Python file uses the following encoding: utf-8

from PySide2.QtWidgets import QApplication
from interface.mainwindow import MainWindow

if __name__ == "__main__":
    app = QApplication([])
    win = MainWindow()
    win.show()
    app.exec_()
