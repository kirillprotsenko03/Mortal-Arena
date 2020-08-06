import pygame
from random import choice
import os


class Map:
    def __init__(self, screen):
        self.screen = screen
        self.rect = []
        self.img_map = pygame.image.load(os.path.join('photo', 'map.bmp'))
        self._create_map()

    def draw(self):
        for rect in self.rect:
            self.screen.blit(self.img_map, rect)

    def _create_map(self):
        x, y = 0, 0
        str_map = self._create_str_map()
        for i in range(200):
            if str_map[i] == '1':
                rect = self.img_map.get_rect()
                rect.x += x
                rect.y += y
                self.rect.append(rect)
            x += 64
            if x == 1280:
                y += 128
                x = 0

    def _create_str_map(self) -> str:
        """создание текстового варианта карты"""
        res = ''
        for i in range(1, 200):
            if i % 20 == 0 and i != 0:
                res += '\n'
            if i % 7 == 0:
                res += str(choice((0, 1)))
            else:
                res += '0'
        return res
