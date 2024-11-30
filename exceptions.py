class PlayerDoesNotExist(Exception):
    '''
    Исключение возникает, если имя пользователя, который должен начать игру не существует
    '''
    def __init__(self):
        self.message = "Такого игрока нет в списке"
        super().__init__(self.message)

