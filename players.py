class Player:
    def __init__(self, name):
        self.name = name


def create_players(players_list=None):
    if players_list is None:
        players_list = []
    players_amount = int(input("Введите количество игроков: "))
    for player in range(players_amount):
        players_list.append(input("Введите имя игрока: "))

    return players_list
