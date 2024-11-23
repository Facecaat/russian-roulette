from manager import Manager

manager_for_players = Manager()

def create_players(players_list=None):
    if players_list is None:
        players_list = []
    players_amount = manager_for_players.amount_of_players()
    players_list = manager_for_players.player_append(players_amount, players_list)

    return players_list

def current_player(player):
    return player