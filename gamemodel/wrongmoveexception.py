# This Python file uses the following encoding: utf-8

class WrongMoveException(Exception):
    '''Exception class raised when the move in the ConnectFour Game is invalid'''
    def __init__(self, column, message="Can't make a move on chosen column!"):
        '''Initializes the exception with the invalid @column and an exception @message'''
        self.column = column
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        '''Returns the string telling on which column the move cannot be made'''
        return f'{self.column + 1} -> {self.message}'
