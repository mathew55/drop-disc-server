import numpy as np
import jsons

ROW_COUNT = 6
COLUMN_COUNT = 9

class Board:
    """
        The Board class which is responsible for initalising & holding
        the state of the GameBoard. It also holds the operations which
        can be performed on the board.

        The board object will be part of a game object.
    """
    def __init__(self):
        self.board = np.zeros((ROW_COUNT, COLUMN_COUNT))

    def is_valid_move(self, col):
        return self.board[ROW_COUNT - 1][col] == 0

    def get_next_valid_row(self, col):
        for r in range(ROW_COUNT):
            if self.board[r][col] == 0:
                return r

    def drop_disc(self, row, col, token):
        self.board[row][col] = token

    def get_board(self):
        return self.board

    def board_as_serialized(self):
        return jsons.dump(self.board)
