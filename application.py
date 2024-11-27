from players import InteractionWithPlayer
from shots import Shots
from manager import Manager

manager = Manager()
player_interaction = InteractionWithPlayer()


class Application:
    def __init__(self):
        self.players = player_interaction.create_players()
        self.shots = Shots()

    def first_move(self, players):
        self.players = players
        return players.index(manager.first_player(self.players))

    def run(self):
        self.current_player = self.players[self.first_move(self.players)]
        global game_run
        game_run = True
        while game_run:
            bullet_counter = 6
            manager.start_game_message()
            for bullet in self.shots.bullets:
                if bullet:
                    manager.shoot_is_good(self.current_player, bullet_counter)
                else:
                    manager.shoot_is_bad(self.current_player)
                    game_run = False
                    break
                bullet_counter -= 1
                self.current_player = player_interaction.next_player(self.current_player, self.players)
                manager.aim_to(self.current_player)
                manager.shoot()
