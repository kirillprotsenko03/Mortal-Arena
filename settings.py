class Setting:
    """ Класс, который хранит основные переменные, влияющие на физикку игры, размер экрана и персонажей и тд"""
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 600
        self.screen_color = (0, 0, 0)

        #  character settings
        self.character_name = 'adventurer'
        self.speed_character = 2
