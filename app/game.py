import jsons

ROW_COUNT = 6
COLUMN_COUNT = 9

game_queue = []

class Game_Logic:

    def check_victory(self, board, token):
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT):
                if board[r][c] == token and board[r][c + 1] == token and board[r][c + 2] == token and board[r][
                    c + 3] == token and board[r][c + 4] == token:
                    return True

        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT - 3):
                if board[r][c] == token and board[r + 1][c] == token and board[r + 2][c] == token and board[r + 3][
                    c] == token and board[r + 4][c] == token:
                    return True

        #TODO : Add logic for diagonal victory checks

class Game:

    turn = 0
    winner = ''
    game_over = False

    def __init__(self, players, board, game_logic):
        self.player1 = players[0]
        self.player2 = players[1]
        self.board = board
        self.game_logic = game_logic
        self.game_id = 1
        self.next_move_player = self.get_next_turn_player()

    def next_turn(self):
        self.turn += 1

    def get_next_turn_player(self):
        if self.turn % 2 == 0:
            return self.player1
        else:
            return self.player2

    def declare_winner(self, player):
        self.game_over = True
        self.winner = player.name

    # def identify_next_move_player(self):
    #     if self.next_move_player == self.player1:
    #         self.next_move_player = self.player2
    #     else:
    #         self.next_move_player = self.player1

    def to_ser_obj(self):
        return jsons.dump(self)