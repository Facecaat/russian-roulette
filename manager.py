class Manager():
    def player_does_not_exists(self):
        print("Такого игрока нет в списке")

    def shoot_is_good(self, player, bullet):
        print(f"{player} выжил. Осталось {bullet} пуль")

    def shoot_is_bad(self, player):
        print(f"{player} прострелил себе голову")
        print("Круг закончен!")

    def first_player(self):
        first_player = input("Введите имя игрока, который начнет игру: ")
        return first_player
