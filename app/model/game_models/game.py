
class Game:

    winner = ''
    game_over = False

    def __init__(self, gameid, players, board, game_logic):

        self.turn = 0
        self.player1 = players[0]
        self.player2 = players[1]
        self.board = board
        self.game_logic = game_logic
        self.game_id = gameid
        self.next_move_player = ''
        self.set_next_turn_player()

    def next_turn(self):
        self.turn += 1
        self.set_next_turn_player()

    def get_next_turn_player(self):
        return self.next_move_player

    def declare_winner(self, player):
        self.game_over = True
        self.winner = player.name

    def set_next_turn_player(self):
        if self.turn % 2 == 0:
            print(self.player1)
            self.next_move_player = self.player1
        else:
            self.next_move_player = self.player2

    def game_state_as_dict(self):
        return{
            "Game_State": {
                "GameID": self.game_id,
                "Player1": self.player1.name,
                "Player2": self.player2.name,
                "Current_Turn_Player": self.next_move_player.name,
                "Board": self.board.board_as_serialized(),
                "Winner": self.winner
            }
        }
