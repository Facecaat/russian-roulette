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
        if self.player != self.players[-1]:
           # self.player != player next
#todo надо current_player подставить того, кого указали первым плеером а потом
#todo итерировать их дальше