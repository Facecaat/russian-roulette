from time import sleep as wait


class MessageManager():
    def bullets_true_naming(self, bullets):
        if bullets in [5, 6]:
            return f"{bullets} пуль"
        elif bullets in [2, 3, 4]:
            return f"{bullets} пули"
        else:
            return f"{bullets} пуля"

    def shoot_is_good(self, player, bullet):
        print(f"{player} выжил. Осталось {self.bullets_true_naming(bullet)}")
        wait(1)

    def shoot_is_bad(self, player):
        print(f"{player} прострелил себе голову")
        print("Игра закончена!")

    def aim_to(self, player):
        print(f"Наводим пистолет на {player}")
        wait(2)

    def shoot(self):
        print("Выстрел!")
        wait(1)

    def start_game_message(self):
        print("Начинаем игру")
