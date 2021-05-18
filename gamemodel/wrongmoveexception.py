# This Python file uses the following encoding: utf-8

class WrongMoveException(Exception):
    def __init__(self, column, message="Can't make a move on chosen column!"):
        self.column = column
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.column + 1} -> {self.message}'
