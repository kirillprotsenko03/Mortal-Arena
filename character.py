import pygame
from images import Image
from game_functions import is_collision


class Character:
    def __init__(self, screen: pygame.Surface, setting, m):
        self.images = Image(setting.character_name)
        self.screen = screen
        self.image = pygame.image.load(self.images.stand_picture)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.x = self.screen_rect.x
        self.rect.y = self.screen_rect.y
        self.speed = setting.speed_character
        self.x, self.y = 0, 0
        self.count_steps = 0
        self.maps_rect = m.rect

    def draw(self) -> None:
        """вывод персонажа на экран"""
        self.screen.blit(self.image, self.rect)

    def move(self) -> None:
        """изменение положения персонажа в пространстве, x и y могут быть либо 0 либо 1 либо -1"""
        old_x, old_y = self.rect.x, self.rect.y
        x = self.rect.x + self.speed * self.x
        y = self.rect.y + self.speed * self.y
        if self.screen_rect.width - self.rect.width > x > 0:
            self.rect.x = x
        if self.screen_rect.height - self.rect.height > y > 0:
            self.rect.y = y
        if self.x != 0 or self.y != 0:
            for m_rect in self.maps_rect:
                if is_collision(self.rect, m_rect):
                    self.rect.x = old_x
                    self.rect.y = old_y

            # изменение картинки при ходьбе
            if self.x == -1:
                self.image = pygame.image.load(self.images.move_picture_left[int(self.count_steps) % 2])
            else:
                self.image = pygame.image.load(self.images.move_picture[int(self.count_steps) % 2])
            self.count_steps += 0.075
        else:
            self.image = pygame.image.load(self.images.stand_picture)
            self.count_steps = 0

    def change_direction(self, x: int, y: int):
        self.x, self.y = x, y
