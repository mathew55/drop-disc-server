from queue import Queue

class Connections:
    player_pool = Queue(10)

    def add_player_to_pool(self, player):
        self.player_pool.put(player)

    def get_size(self):
        return self.player_pool.qsize()

    def get_next_waiting_player(self):
        return self.player_pool.get()



