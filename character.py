import pygame
import os


class Character:
    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen
        path = os.path.join('photo', 'adventurer_stand.bmp')
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def draw_character(self) -> None:
        """вывод персонажа на экран"""
        self.screen.blit(self.image, self.rect)
