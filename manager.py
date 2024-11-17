class Manager():
    def player_does_not_exists(self):
        return "Такого игрока нет в списке"

    def shoot_is_good(self, player, bullet):
        print(f"{player} выжил. Осталось {bullet} пуль")

    def shoot_is_bad(self, player):
        print(f"{player} прострелил себе голову")
        print("Круг закончен!")

    def first_player(self):
        first_player = input("Введите имя игрока, который начнет игру: ")
        return first_player

    def amount_of_players(self):
        players_amount = int(input("Введите количество игроков: "))
        return players_amount

    def player_append(self, amount, players_list):
        for player in range(amount):
            players_list.append(input("Введите имя игрока: "))
        return players_list

