def player_does_not_exists():
    print("Такого игрока нет в списке")

def shoot_is_good(player, bullet):
    print(f"{player} выжил. Осталось {bullet} пуль")

def shoot_is_bad(player):
    print(f"{player} прострелил себе голову")
    print("Круг закончен!")