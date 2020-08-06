import os


class Image:
    def __init__(self, name_character: str):
        self.stand_picture = self._stand_picture(name_character)
        self.move_picture = self._move_picture(name_character)
        self.move_picture_left = self._move_picture_left(name_character)

    def _stand_picture(self, name: str) -> str:
        """возвращает путь к изображению, где персонаж стоит"""
        name_picture = name + '_stand.bmp'
        full_path = os.path.join('photo', name_picture)
        return full_path

    def _move_picture(self, name: str) -> tuple:
        """возвращает пути к изображению, где персонаж гуляет"""
        name_picture_1 = name + '_walk1.bmp'
        name_picture_2 = name + '_walk2.bmp'
        full_path_1 = os.path.join('photo', name_picture_1)
        full_path_2 = os.path.join('photo', name_picture_2)
        return full_path_1, full_path_2

    def _move_picture_left(self, name: str) -> tuple:
        name_picture_1 = name + '_walkleft1.bmp'
        name_picture_2 = name + '_walkleft2.bmp'
        full_path_1 = os.path.join('photo', name_picture_1)
        full_path_2 = os.path.join('photo', name_picture_2)
        return full_path_1, full_path_2
