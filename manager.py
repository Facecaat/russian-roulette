from time import sleep as wait


class Manager():
    def bullets_true_naming(self, bullets):
        if bullets in [5, 6]:
            return f"{bullets} пуль"
        elif bullets in [2, 3, 4]:
            return f"{bullets} пули"
        else:
            return f"{bullets} пуля"

    def player_does_not_exists(self):
        return "Такого игрока нет в списке"

    def players_amount_is_not_correct(self):
        return "Количество игроков должно быть от 2 до 6"

    def shoot_is_good(self, player, bullet):
        print(f"{player} выжил. Осталось {self.bullets_true_naming(bullet)}")

    def shoot_is_bad(self, player):
        print(f"{player} прострелил себе голову")
        print("Игра закончена!")

    def aim_to(self, player):
        print(f"Наводим пистолет на {player}")
        wait(1)

    def shoot(self):
        print("Выстрел!")
        wait(1)

    def first_player(self):
        first_player = input("Введите имя игрока, который начнет игру: ")
        return first_player

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

    def player_append(self, amount, players_list):
        for player in range(amount):
            players_list.append(input("Введите имя игрока: "))
        return players_list

    def start_game_message(self):
        print("Начинаем игру")
