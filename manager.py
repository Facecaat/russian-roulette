from exceptions import PlayerDoesNotExist, PlayerAlreadyExist, WrongPlayersAmount


class Manager():

#удалить два нижних def и добавить их ексепшенами ниже
    def players_amount_is_not_correct(self):
        return "Количество игроков должно быть от 2 до 6"

    def player_name_already_exist(self):
        return "Такое имя игрока уже есть"

    def first_player(self, players):
        while True:
            try:
                first_player = input("Введите имя игрока, который начнет игру: ")
                if first_player in players:
                    return first_player
                else:
                    raise PlayerDoesNotExist
            except PlayerDoesNotExist as e:
                print(e.message)

    def amount_of_players(self):
        while True:
            try:
                self.players_amount = int(input("Введите количество игроков: "))
                if 2 <= self.players_amount <= 6:
                    break
                else:
                    raise ValueError
            except ValueError as e:
                print(self.players_amount_is_not_correct())
        return self.players_amount

    def name_does_not_exist(self, players):
        while True:
            name = input("Введите имя игрока: ")
            if name not in players:
                return name
            else:
                print(self.player_name_already_exist())

    def player_append(self, amount, players_list):
        for player in range(amount):
            player_name = self.name_does_not_exist(players_list)
            if player_name:
                players_list.append(player_name)
            else:
                break
        return players_list
