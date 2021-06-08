# This Python file uses the following encoding: utf-8

from PySide2.QtWidgets import QDialog, QLabel, QPushButton, QWidget, QVBoxLayout
from PySide2.QtGui import QFont
from PySide2.QtCore import QSize, Qt


class GameStateDialog(QDialog):
    '''Dialog used to display important game events (player won, game drawn)'''
    def __init__(self, game_state):
        '''Initialize the font, properties and widgets of the dialog based on the @game_state'''
        super().__init__()
        self.set_font()
        self.set_window_properties()
        self.set_window_widgets(game_state)

    def set_font(self):
        '''Sets the font for the whole dialog'''
        self.font = QFont("Comic Sans MS", 15)
        self.font.setBold(True)

    def set_window_properties(self):
        '''Sets the size and other properties of the dialog'''
        self.setWindowTitle("GG")
        self.setFixedSize(QSize(180, 100))
        self.central_widget = QWidget(self)
        self.central_layout = QVBoxLayout(self.central_widget)
        self.setModal(True)

    def set_window_widgets(self, game_state):
        '''Sets the apperance of the dialog widgets based on the @game_state'''
        self.info_label = QLabel(self.central_widget)
        self.central_layout.addWidget(self.info_label)
        if game_state != 0:
            self.info_label.setText("Player " + str(game_state) + " won!")
        else:
            self.info_label.setText("Game drawn!")
        self.info_label.setFont(self.font)
        self.central_layout.setAlignment(self.info_label, Qt.AlignHCenter)

        self.ok_button = QPushButton(self.central_widget)
        self.central_layout.addWidget(self.ok_button)
        self.font.setPointSize(10)
        self.ok_button.setText("OK")
        self.ok_button.setFont(self.font)
        self.ok_button.clicked.connect(lambda: self.accept())
        self.central_layout.setAlignment(self.ok_button, Qt.AlignHCenter)
