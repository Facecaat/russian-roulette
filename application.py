from players import InteractionWithPlayer

from shots import Shots
from manager import Manager

manager = Manager()
player_interaction = InteractionWithPlayer()


class Application:
    def __init__(self):
        self.players = player_interaction.create_players()
        self.shots = Shots()
        self.current_player = player_interaction.current_player(self.players[0])
        self.next_player = player_interaction.next_player(self.current_player, self.players)

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
        global game_run
        game_run = True
        while game_run:
            manager.start_game_message()
            manager.pause(2)
            for bullet in self.shots.bullets:
                if bullet:
                    print(f"{self.current_player} выжил")
                else:
                    print(f"{self.current_player} погиб")
                    game_run = False
                    break
                self.current_player = player_interaction.next_player(self.current_player, self.players)
                print(f"Наводим пистолет на {self.current_player}")
                manager.pause(1)
                print("Выстрел!")
                manager.pause(1)
