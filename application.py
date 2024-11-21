from players import create_players

from shots import Shots
from manager import Manager


manager = Manager()


class Application:
    def __init__(self):
        self.players = create_players()
        self.shots = Shots()
        self.current_player_index = 0

    def first_move(self, players):
        name_is_correct = True
        self.players = players
        while name_is_correct:
            try:
                first_player = manager.first_player()
                if first_player not in self.players:
                    raise ValueError
                name_is_correct = False
            except ValueError as e:
                print(manager.player_does_not_exists())

    def run(self):
        self.first_move(self.players)
        while True:
            manager.start_game_message()
            manager.pause(2)
            for bullet in self.shots.bullets:
                if bullet:
                    print("Игрок выжил")
                else:
                    print("Игрок умер")



