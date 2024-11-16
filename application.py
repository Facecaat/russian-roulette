from players import create_players
from time import sleep as wait
from random import randint as rand

players = create_players()


class Application:
    def first_move(self, players):
        name_is_correct = True
        self.players = players
        while name_is_correct:
            try:
                first_player = input("Введите имя игрока, который начнет игру: ")
                if first_player not in self.players:
                    raise ValueError
                name_is_correct = False
            except ValueError as e:
                print("Такого игрока нет в списке")

    def run(self):
        self.first_move(players)
        while True:
            wait(2)
            print("Игрок выжил" if rand(1, 2) == 2 else "Игрок помер")
