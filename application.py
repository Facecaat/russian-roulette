from players import create_players
from time import sleep as wait
from shots import Shots
from manager import Manager

players = create_players()
manager = Manager()

class Application:

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
                manager.player_does_not_exists()

    def run(self):
        self.first_move(players)
        while True:
            test = input("Программа в run: ")

