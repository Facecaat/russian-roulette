class PlayerDoesNotExist(Exception):
    '''
    Исключение возникает, если имя пользователя, который должен начать игру не существует
    '''

    def __init__(self):
        self.message = "Такого игрока нет в списке"
        super().__init__(self.message)


class PlayerAlreadyExist(Exception):
    '''
    Исключение возникает, если такой игрок уже есть в списке
    '''

    def __init__(self):
        self.message = "Такого имя игрока уже есть"
        super().__init__(self.message)


class WrongPlayersAmount(Exception):
    '''
    Исключение возникает когда количество игроков меньше 2 или больше 6
    '''

    def __init__(self):
        self.message = "Количество игроков должно быть от 2 до 6"
        super().__init__(self.message)
