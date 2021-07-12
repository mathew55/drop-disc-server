from app.context.app_context import ApplicationContext
from app.model.game_models.game import Game
from app.model.game_models.board import Board
from app.services.game_logic import Game_Logic
import time

board = Board()
game_logic = Game_Logic()
cx = ApplicationContext.getContext()


class PlayerMatcher:

    def add_player_to_pool(self, player):
        cx.player_pool.put(player)

    def get_size(self):
        return cx.player_pool.qsize()

    def get_next_waiting_player(self):
        return cx.player_pool.get()

    def start_match(self):
        print(f"Size - {self.get_size()}")
        while (self.get_size() % 2) != 0:
            True

        with cx.player_pool.mutex:
            player_list = list(cx.player_pool.queue)
            player1 = player_list[0]
            player2 = player_list[1]
            gameid = player1.name + player2.name

        time.sleep(0.5)
        with cx.player_pool.mutex:
            print(f"Hey this is my game id {gameid}")
            game = Game(gameid, [player1, player2], board, game_logic)
            cx.game_queue_map[gameid] = game
            if gameid in cx.game_queue_map.keys():
                print("Gameid exists")
            else:
                print("GameId does not exists")
                cx.game_queue_map[gameid] = game
            cx.player_pool.queue.clear()
            return cx.game_queue_map[gameid]



