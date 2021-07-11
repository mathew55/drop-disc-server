from app.game import Game_Logic
from app.game import Game
from app.game import game_queue
from app.board import Board
import json
import queue

board = Board()
game_logic = Game_Logic()

class Connections:
    connection_queue = []

    def add_player_to_connection_queue(self,player):
        self.connection_queue.append(player)

    def display_players(self):
        print(f"Current Players in the list - {self}")

    def start_match(self):
        print(f"Size - {len(self.connection_queue)}")
        while (len(self.connection_queue) % 2) != 0:
            True

        game = Game([self.connection_queue[0], self.connection_queue[1]], board, game_logic)

        game_queue.append(game)
        return game

    def __str__(self):
        players = ''
        for player in self.connection_queue:
            players = players+ ', ' + player.name

        return players
