from random import randint as rand, shuffle as shuf

class Shots:
    def __init__(self):
        self.bullets = [True] * 5 + [False]
        shuf(self.bullets)

    def shoot(self):
        pass

#todo добавь перемешку true и false и итерируясь по bullets будет решать сдох
#todo или не сдох