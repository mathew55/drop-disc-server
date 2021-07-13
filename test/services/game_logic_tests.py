import unittest
import numpy as np
from app.services.game_logic import Game_Logic


game_logic = Game_Logic()

class TestGameLogic(unittest.TestCase):

    def test_empty_numpy(self):
        board = np.zeros((6, 9))
        token = 1

        test_output = game_logic.check_victory(board, token)
        expected_output = None
        print(test_output)
        self.assertEquals(test_output, expected_output)

    def test_vertical_numpy(self):
        board = np.array([[1, 0, 0, 0, 0, 0, 0, 0, 0],
                          [1, 0, 0, 0, 0, 0, 0, 0, 0],
                          [1, 0, 0, 0, 0, 0, 0, 0, 0],
                          [1, 0, 0, 0, 0, 0, 0, 0, 0],
                          [1, 0, 0, 0, 0, 0, 0, 0, 0],
                          [1, 0, 0, 0, 0, 0, 0, 0, 0],
                          ])
        token = 1

        test_output = game_logic.check_victory(board, token)
        expected_output = True
        print(test_output)
        self.assertEquals(test_output, expected_output)

    def test_horizontal_numpy(self):
        board = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [1, 1, 1, 1, 1, 0, 0, 0, 0],
                          ])
        token = 1

        test_output = game_logic.check_victory(board, token)
        expected_output = True
        print(test_output)
        self.assertEquals(test_output, expected_output)

    def test_diagonal_numpy(self):
        board = np.array([[0, 0, 1, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 1, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 1, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 1, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 1, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0],
                          ])
        token = 1

        test_output = game_logic.check_victory(board, token)
        expected_output = True
        print(test_output)
        self.assertEquals(test_output, expected_output)