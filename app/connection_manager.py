from queue import Queue
from app.context.app_context import ApplicationContext
from app.model.game_models.game import Game
from app.game import Game_Logic
from app.model.game_models.game import Game
from app.board import Board

board = Board()
game_logic = Game_Logic()
cx = ApplicationContext.getContext()
class Connections:
    player_pool = []

    def add_player_to_pool(self, player):
        self.player_pool.append(player)

    def get_size(self):
        # return self.player_pool.qsize()
        return len(self.player_pool)

    def get_next_waiting_player(self):
        return self.player_pool.get()

    def start_match(self):
        print(f"Size - {self.get_size()}")
        while (self.get_size() % 2) != 0:
            True

        player1 = self.player_pool[0]
        player2 = self.player_pool[1]

        game = Game([player1, player2], board, game_logic)

        cx.game_queue.append(game)
        return game




