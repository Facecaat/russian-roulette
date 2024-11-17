from random import randint as rand

class Shots:
    def __init__(self):
        self.bullets = [True] * 6
        self.deadly_bullet = rand(1,6)

    def shoot(self):
        pass
