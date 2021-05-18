# This Python file uses the following encoding: utf-8
from PySide2.QtWidgets import (QApplication, QMainWindow, QGridLayout, QVBoxLayout,
                                QHBoxLayout, QPushButton, QWidget, QLabel, QComboBox)
from PySide2.QtGui import QPixmap, QFont
from PySide2.QtCore import QSize, Qt
from itertools import chain
from gamemodel.connectfour import ConnectFourClassic, ConnectFourPopOut
from gamemodel.wrongmoveexception import WrongMoveException
import gamestatedialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.game = ConnectFourClassic()
        self.init_interface()
        self.init_backend()

    def init_interface(self):
        self.set_font()
        self.set_window_properties()
        self.set_top_controls()
        self.set_game_board()
        self.set_bottom_controls()
        self.set_menu()

    def set_font(self):
        # font will be used in styling the text in the widgets
        self.font = QFont("Comic Sans MS", 10)
        self.font.setBold(True)

    def set_window_properties(self):
        self.setWindowTitle("Connect Four")
        self.setFixedSize(QSize(720, 825))
        # setting central layout for all the game components
        self.setCentralWidget(QWidget(self))
        self.central_layout = QVBoxLayout(self.centralWidget())

    def set_top_controls(self):
        # top controls will be used to drop the coins on the board
        self.top_controls_widget = QWidget(self.centralWidget())
        self.central_layout.addWidget(self.top_controls_widget)
        self.top_controls_layout = QHBoxLayout(self.top_controls_widget)
        self.create_drop_buttons()

    def set_game_board(self):
        self.board_widget = QWidget(self.centralWidget())
        self.central_layout.addWidget(self.board_widget)
        self.board_layout = QGridLayout(self.board_widget)
        self.board_layout.setVerticalSpacing(0)
        self.board_layout.setHorizontalSpacing(0)
        self.board_layout.setOriginCorner(Qt.BottomLeftCorner)
        self.render_board()

    def set_bottom_controls(self):
        # bottom controls will be used to pop the coins from the board
        self.bottom_controls_widget = QWidget(self.centralWidget())
        self.central_layout.addWidget(self.bottom_controls_widget)
        self.bottom_controls_layout = QHBoxLayout(self.bottom_controls_widget)
        self.create_pop_buttons()

    def set_menu(self):
        self.menu_widget = QWidget(self.centralWidget())
        self.central_layout.addWidget(self.menu_widget)
        self.menu_layout = QHBoxLayout(self.menu_widget)
        # button to start the game or reset
        self.font.setPointSize(20)
        self.start_restart_button = QPushButton(self.menu_widget)
        self.start_restart_button.setText("Start")
        self.start_restart_button.setFont(self.font)
        self.menu_layout.addWidget(self.start_restart_button)
        # combo box with 2 game modes to choose from
        self.game_mode_combo_box = QComboBox(self.menu_widget)
        self.game_mode_combo_box.addItem("Classic")
        self.game_mode_combo_box.addItem("PopOut")
        self.game_mode_combo_box.setFont(self.font)
        self.menu_layout.addWidget(self.game_mode_combo_box)
        self.game_mode_combo_box.currentIndexChanged.connect(
            lambda *args: self.set_game_mode(self.game_mode_combo_box.currentText()))
        # information label to notify the user about the state of the game
        self.font.setPointSize(15)
        self.info_label = QLabel(self.menu_widget)
        self.info_label.setFixedSize(QSize(350, 40))
        self.info_label.setText("Waiting for start...")
        self.info_label.setFont(self.font)
        self.info_label.setAlignment(Qt.AlignCenter)
        self.menu_layout.addWidget(self.info_label)

    def set_game_mode(self, mode):
        '''Sets the game mode to one provided'''
        self.game_mode = mode
        if self.game_mode == "PopOut":
            self.game = ConnectFourPopOut()
        elif self.game_mode == "Classic":
            self.game = ConnectFourClassic()

    def create_drop_buttons(self):
        '''Creates 7 drop buttons displayed on the top control bar'''
        self.drop_buttons = []
        for i in range(7):
            code = ("self.drop_button" + str(i + 1) + " = QPushButton(self.top_controls_widget)\n" +
                "self.drop_buttons.append(self.drop_button" + str(i + 1) +")")
            exec(code)
            self.top_controls_layout.addWidget(self.drop_buttons[i])
            self.drop_buttons[i].setText("Drop c. " + str(i + 1))
            self.drop_buttons[i].setFont(self.font)
            self.drop_buttons[i].setEnabled(False)

    def create_pop_buttons(self):
        '''Creates 7 pop buttons displayed on the bottom control bar'''
        self.pop_buttons = []
        for i in range(7):
            code = ("self.pop_button" + str(i + 1) + " = QPushButton(self.bottom_controls_widget)\n" +
                "self.pop_buttons.append(self.pop_button" + str(i + 1) +")")
            exec(code)
            self.bottom_controls_layout.addWidget(self.pop_buttons[i])
            self.pop_buttons[i].setText("Pop c. " + str(i + 1))
            self.pop_buttons[i].setFont(self.font)
            self.pop_buttons[i].setEnabled(False)

    def render_board(self):
        '''Updates the board's visual appearance'''
        positions = list(chain.from_iterable([[(i, j) for j in range(7)] for i in range(6)]))
        for position in positions:
            self.render_field(position[0], position[1])

    def render_field(self, x, y):
        '''Updates a single board field's appearance'''
        field = QLabel(self.board_widget)
        if self.game.get_board()[x][y] == 1:
            field.setPixmap((QPixmap("drawable/red_field.png")))
        elif self.game.get_board()[x][y] == 2:
            field.setPixmap((QPixmap("drawable/yellow_field.png")))
        else:
            field.setPixmap((QPixmap("drawable/empty_field.png")))
        self.board_layout.addWidget(field, x, y)

    def init_backend(self):
        self.game_in_progress = False
        self.game_mode = self.game_mode_combo_box.currentText()
        # connecting the start/restart button with the function handling the click
        self.start_restart_button.clicked.connect(self.start_restart_game)
        # connecting the click events of each game buttons to their corresponding action function
        for drop_button, pop_button, column in zip(self.drop_buttons, self.pop_buttons, range(7)):
            drop_button.clicked.connect(lambda *args, column=column: self.drop_move(column))
            pop_button.clicked.connect(lambda *args, column=column: self.pop_move(column))

    def start_restart_game(self):
        '''Based on the current game state either starts the game or resets the game'''
        if self.game_in_progress:
            self.game_in_progress = False
            self.start_restart_button.setText("Start")
            self.info_label.setText("Waiting for start...")
            self.game_mode_combo_box.setEnabled(True)
            self.enable_control_buttons(False)
            self.game.reset()
            self.render_board()
        else:
            self.game_in_progress = True
            self.start_restart_button.setText("Restart")
            self.info_label.setText("Player " + str(self.game.current_player) + " turn!")
            self.game_mode_combo_box.setEnabled(False)
            self.enable_control_buttons(True)

    def enable_control_buttons(self, enable):
        '''Based on the enable parameter and the game mode either enables or disables the control buttons'''
        for pop, drop in zip(self.pop_buttons, self.drop_buttons):
            drop.setEnabled(enable)
            if enable:
                if self.game_mode == "PopOut":
                    pop.setEnabled(enable)
            else:
                pop.setEnabled(enable)

    def move(move_func):
        '''A wrapper function for any type of move during the game'''

        def wrap(self, *args, **kwargs):
            try:
                move_func(self, *args, **kwargs)
                self.render_board()
            except WrongMoveException:
                self.info_label.setText("Can't make a move here!")
        return wrap

    @move
    def drop_move(self, column):
        '''Drops the current player's coin on the specified column'''
        self.game.drop_move(column)
        if self.game.is_winning(self.game.current_player):
            self.info_label.setText("Player " + str(self.game.current_player) + " won!")
            self.enable_control_buttons(False)
            dialog = gamestatedialog.GameStateDialog(self.game.current_player)
            dialog.show()
        elif self.game.is_board_full() and self.game_mode == "Classic":
            self.info_label.setText("Game drawn!")
            self.enable_control_buttons(False)
            dialog = gamestatedialog.GameStateDialog(0)
            dialog.show()
        else:
            self.game.change_turns()
            self.info_label.setText("Player " + str(self.game.current_player) + " turn!")

    @move
    def pop_move(self, column):
        '''Pops the current player's column from the specified column'''
        self.game.pop_move(column)
        if self.game.is_winning(self.game.current_player):
            self.info_label.setText("Player " + str(self.game.current_player) + " won!")
            self.enable_control_buttons(False)
            dialog = gamestatedialog.GameStateDialog(self.game.current_player)
            dialog.show()
        elif self.game.is_winning(self.game.next_player):
            self.info_label.setText("Player " + str(self.game.next_player) + " won!")
            self.enable_control_buttons(False)
            dialog = gamestatedialog.GameStateDialog(self.game.next_player)
            dialog.show()
        else:
            self.game.change_turns()
            self.info_label.setText("Player " + str(self.game.current_player) + " turn!")


if __name__ == "__main__":
    app = QApplication([])
    win = MainWindow()
    win.show()
    app.exec_()
