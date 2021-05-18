# This Python file uses the following encoding: utf-8

from gamemodel.wrongmoveexception import WrongMoveException


class ConnectFourBase:
    def __init__(self):
        self.current_player = 1
        self.next_player = 2
        self.row_count = 6
        self.column_count = 7
        self.board = self.get_new_board()

    def get_new_board(self):
        '''Returns empty (filled with zeros) 6x7 game board'''
        return [[0 for i in range(self.column_count)] for i in range(self.row_count)]

    def get_board(self):
        '''Returns the current board'''
        return self.board

    def reset(self):
        '''Resets the game state'''
        self.board = self.get_new_board()
        self.current_player = 1

    def is_board_full(self):
        '''Returns True if there is no more free place on the board'''
        return not any(0 in row for row in self.board)

    def change_turns(self):
        '''Makes the current player the next player'''
        self.current_player = self.next_player
        self.next_player = 1 if self.next_player == 2 else 2

    def drop_move(self, column):
        '''Drops the coin of the current player on the specified column'''
        raise NotImplementedError('drop_move is not implemented')

    def is_valid_drop(self, column):
        '''Returns True if the drop on the specified column is possible'''
        raise NotImplementedError('is_valid_drop is not implemented')

    def is_winning(self, player):
        '''Returns True if the player wins the game'''
        raise NotImplementedError('is_winning is not implemented')


class ConnectFourClassic(ConnectFourBase):
    def __init__(self):
        super().__init__()

    def drop_move(self, column):
        if self.is_valid_drop(column):
            for row in self.board:
                if row[column] == 0:
                    row[column] = self.current_player
                    return
        else:
            raise WrongMoveException(column)

    def is_valid_drop(self, column):
        if self.board[self.row_count - 1][column] != 0:
            return False
        else:
            return True

    def is_winning(self, player):
        # horizontal
        for col in range(self.column_count - 3):
            for row in range(self.row_count):
                if (self.board[row][col] == player
                        and self.board[row][col + 1] == player
                        and self.board[row][col + 2] == player
                        and self.board[row][col + 3] == player):
                    return True

        # vertical
        for col in range(self.column_count):
            for row in range(self.row_count - 3):
                if (self.board[row][col] == player
                        and self.board[row + 1][col] == player
                        and self.board[row + 2][col] == player
                        and self.board[row + 3][col] == player):
                    return True

        # positively sloped diagonals
        for col in range(self.column_count - 3):
            for row in range(self.row_count - 3):
                if (self.board[row][col] == player
                        and self.board[row + 1][col + 1] == player
                        and self.board[row + 2][col + 2] == player
                        and self.board[row + 3][col + 3] == player):
                    return True

        # negatively sloped diagonals
        for col in range(self.column_count - 3):
            for row in range(3, self.row_count):
                if (self.board[row][col] == player
                        and self.board[row - 1][col + 1] == player
                        and self.board[row - 2][col + 2] == player
                        and self.board[row - 3][col + 3] == player):
                    return True

        return False


class ConnectFourPopOut(ConnectFourBase):
    def __init__(self):
        super().__init__()

    def drop_move(self, column):
        if self.is_valid_drop(column):
            for row in self.board:
                if row[column] == 0:
                    row[column] = self.current_player
                    return
        else:
            raise WrongMoveException(column)

    def is_valid_drop(self, column):
        if self.board[self.row_count - 1][column] != 0:
            return False
        else:
            return True

    def pop_move(self, column):
        '''Pops the coin of the current player from the specified column'''
        if self.is_valid_pop(column):
            for i in range(self.row_count - 1):
                self.board[i][column] = self.board[i + 1][column]
            self.board[self.row_count - 1][column] = 0
        else:
            raise WrongMoveException(column)

    def is_valid_pop(self, column):
        '''Returns True if the pop from the specified column is possible'''
        return self.board[0][column] == self.current_player

    def is_winning(self, player):
        # horizontal
        for col in range(self.column_count - 3):
            for row in range(self.row_count):
                if (self.board[row][col] == player
                        and self.board[row][col + 1] == player
                        and self.board[row][col + 2] == player
                        and self.board[row][col + 3] == player):
                    return True

        # vertical
        for col in range(self.column_count):
            for row in range(self.row_count - 3):
                if (self.board[row][col] == player
                        and self.board[row + 1][col] == player
                        and self.board[row + 2][col] == player
                        and self.board[row + 3][col] == player):
                    return True

        # positively sloped diagonals
        for col in range(self.column_count - 3):
            for row in range(self.row_count - 3):
                if (self.board[row][col] == player
                        and self.board[row + 1][col + 1] == player
                        and self.board[row + 2][col + 2] == player
                        and self.board[row + 3][col + 3] == player):
                    return True

        # negatively sloped diagonals
        for col in range(self.column_count - 3):
            for row in range(3, self.row_count):
                if (self.board[row][col] == player
                        and self.board[row - 1][col + 1] == player
                        and self.board[row - 2][col + 2] == player
                        and self.board[row - 3][col + 3] == player):
                    return True

        return False
