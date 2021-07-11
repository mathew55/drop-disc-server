from flask import Flask
from app.connection_manager import Connections
from app.board import Board
import jsons
from app.game import game_queue
import json
from move import next_board_move
from move import next_player
from app.player import Player
from flask import request

app = Flask(__name__)
connection_pool = Connections()

@app.route('/healthcheck')
def health_check():
    """Print 'Hello, world!' as the response body."""
    return 'Drop-Disc-Server is Up & Running'


@app.route('/start-game/', methods= ["POST"])
def start_game():
    player_name = request.args.get("player_name")
    print(f"Welcome to the game {player_name}")
    player = Player(player_name, 1)
    print(f"Player - {player}")
    connection_pool.add_player_to_connection_queue(player)
    game = connection_pool.start_match()
    print(f"Game started - {game}")
    return f"{json.dumps(game.to_ser_obj())}"


@app.route('/next-move/', methods= ["POST"])
def make_move():
    game_id = 1
    move_col = int(request.args.get("move_col"))
    game = next_board_move(game_id, move_col)
    return f"{json.dumps(game)}"

@app.route('/get-player/', methods= ["POST"])
def current_player():
    game_id = 1
    game = next_player(1)
    return f"{json.dumps(game.to_ser_obj())}"


if __name__ == '__main__':
    app.debug=True
    app.run()