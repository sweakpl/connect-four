# This Python file uses the following encoding: utf-8

import unittest
from gamemodel.connectfour import ConnectFourClassic
from gamemodel.wrongmoveexception import WrongMoveException


class ConnectFourTest(unittest.TestCase):
    '''TestCase class for testing the ConnectFourClassic functionalities'''

    def setUp(self):
        self.game = ConnectFourClassic()

    def test_should_board_contain_two_coins_when_two_drops(self):
        '''After two moves the board contains two coins'''
        # given

        # when
        self.game.drop_move(0)
        self.game.change_turns()
        self.game.drop_move(1)
        expected_board = [[0 for i in range(7)] for i in range(6)]
        expected_board[0][0] = 1
        expected_board[0][1] = 2

        # then
        self.assertEqual(self.game.board, expected_board)

    def test_should_return_true_when_vertical_win_line(self):
        '''is_winning(1) returns True when the player 1 assembles vertical winning line'''
        # given
        self.game.board = [[1, 2, 0, 0, 0, 0, 0],
                           [1, 2, 0, 0, 0, 0, 0],
                           [1, 2, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0]]

        # when
        self.game.drop_move(0)
        is_player_one_winning = self.game.is_winning(1)

        # then
        self.assertTrue(is_player_one_winning)

    def test_should_return_true_when_horizontal_win_line(self):
        '''is_winning(1) returns True when the player 1 assembles horizontal winning line'''
        # given
        self.game.board = [[1, 1, 1, 0, 0, 0, 0],
                           [2, 2, 2, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0]]

        # when
        self.game.drop_move(3)
        is_player_one_winning = self.game.is_winning(1)

        # then
        self.assertTrue(is_player_one_winning)

    def test_should_return_true_when_diagonal_win_line(self):
        '''is_winning(1) returns True when the player 1 assembles diagonal winning line'''
        # given
        self.game.board = [[1, 2, 1, 2, 0, 0, 0],
                           [0, 1, 2, 2, 0, 0, 0],
                           [0, 0, 1, 1, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0]]

        # when
        self.game.drop_move(3)
        is_player_one_winning = self.game.is_winning(1)

        # then
        self.assertTrue(is_player_one_winning)

    def test_should_return_true_when_board_tied(self):
        '''is_board_full() returns True if there is no more free space on the board'''
        # given
        self.game.board = [[2, 2, 2, 1, 2, 2, 2],
                           [1, 1, 1, 2, 1, 1, 1],
                           [2, 2, 2, 1, 2, 2, 2],
                           [1, 1, 1, 2, 1, 1, 1],
                           [2, 2, 2, 1, 2, 2, 2],
                           [1, 1, 1, 2, 1, 1, 1]]

        # when
        is_game_tied = self.game.is_board_full()

        # then
        self.assertTrue(is_game_tied)

    def test_should_return_true_when_longer_than_four_win_line(self):
        '''is_winning(1) returns True when the player 1 assembles winning line longer than four coins'''
        # given
        self.game.board = [[1, 1, 1, 0, 1, 1, 1],
                           [2, 2, 2, 0, 2, 2, 2],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0]]

        # when
        self.game.drop_move(3)
        is_player_one_winning = self.game.is_winning(1)

        # then
        self.assertTrue(is_player_one_winning)

    def test_should_throw_wrong_move_exception_when_wrong_drop(self):
        '''drop_move(0) raises WrongMoveException when the column 0 is full'''
        # given
        self.game.board = [[2, 0, 0, 0, 0, 0, 0],
                           [1, 0, 0, 0, 0, 0, 0],
                           [2, 0, 0, 0, 0, 0, 0],
                           [1, 0, 0, 0, 0, 0, 0],
                           [2, 0, 0, 0, 0, 0, 0],
                           [1, 0, 0, 0, 0, 0, 0]]

        # when

        # then
        self.assertRaises(WrongMoveException, self.game.drop_move, 0)


if __name__ == "__main__":
    unittest.main()
