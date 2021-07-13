from app.context.app_context import ApplicationContext
from app.model.game_models.game import Game
from app.model.game_models.board import Board
from app.services.game_logic import Game_Logic
import time

board = Board()
game_logic = Game_Logic()
cx = ApplicationContext.getContext()


class PlayerMatcher:
    """
        Player matcher class which is responsible for matching players based on the
        available players in the player pool
    """

    def add_player_to_pool(self, player):
        """Adds player for pool"""
        cx.player_pool.put(player)

    def get_size(self):
        return cx.player_pool.qsize()

    def get_next_waiting_player(self):
        return cx.player_pool.get()

    def start_match(self):
        """
        Starts the match if there are a pair of players in the pool, Otherwise waits till
        a new player joins the game

        Uses locks to ensure consistency while updating the game state.
        Also adds the newly created game to game_queue.
        :return: Initial game state
        """
        while (self.get_size() % 2) != 0:
            True

        with cx.player_pool.mutex:
            player_list = list(cx.player_pool.queue)
            player1 = player_list[0]
            player2 = player_list[1]
            gameid = player1.name + player2.name

        time.sleep(0.5)
        with cx.player_pool.mutex:
            game = Game(gameid, [player1, player2], board, game_logic)
            cx.game_queue_map[gameid] = game
            if gameid in cx.game_queue_map.keys():
                cx.log.info(f"The GameID Already exists in memory, {gameid}")
            else:
                cx.log.info(f"GameId does not exists, Creating the game {gameid}")
                cx.game_queue_map[gameid] = game
            cx.player_pool.queue.clear()
            return cx.game_queue_map[gameid]



