from manager import Manager

manager_for_players = Manager()


class InteractionWithPlayer:
    def create_players(self, players_list=None):
        if players_list is None:
            players_list = []
        players_amount = manager_for_players.amount_of_players()
        players_list = manager_for_players.player_append(players_amount, players_list)

        return players_list

    def current_player(self, player):
        self.player = player
        return self.player

    def next_player(self, player, players):
        self.player = player
        self.players = players
        self.player_index = self.players.index(self.player)
        if self.player == self.players[-1]:
            self.player = self.players[0]
        else:
            self.player = self.players[self.player_index + 1]
        return self.player
