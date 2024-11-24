from random import randint as rand, shuffle as shuf


class Shots:
    def __init__(self):
        self.bullets = [True] * 5 + [False]
        shuf(self.bullets)

