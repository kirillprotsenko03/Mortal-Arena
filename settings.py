class Setting:
    """ Класс, который хранит основные переменные, влияющие на физикку игры, размер экрана и персонажей и тд"""
    def __init__(self):
        self.screen_width = 1280
        self.screen_height = 640
        self.screen_color = (0, 0, 0)

        #  character settings
        self.character_name = 'adventurer'
        self.speed_character = 5
