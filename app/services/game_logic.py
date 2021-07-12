ROW_COUNT = 6
COLUMN_COUNT = 9

class Game_Logic:

    def check_victory(self, board, token):
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT):
                if board[r][c] == token and board[r][c + 1] == token and board[r][c + 2] == token and \
                        board[r][c + 3] == token and board[r][c + 4] == token:
                    return True

        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT - 3):
                if board[r][c] == token and board[r + 1][c] == token and board[r + 2][c] == token and \
                        board[r + 3][c] == token and board[r + 4][c] == token:
                    return True

        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT - 3):
                if board[r][c] == token and board[r + 1][c + 1] == token and board[r + 2][c + 2] == token and \
                        board[r + 3][c + 3] == token and board[r + 4][c + 4] == token:
                    return True

        for c in range(COLUMN_COUNT - 3):
            for r in range(3, ROW_COUNT):
                if board[r][c] == token and board[r - 1][c + 1] == token and board[r - 2][c + 2] == token and \
                        board[r - 3][c + 3] == token and board[r - 4][c - 4] == token:
                    return True
