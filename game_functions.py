import pygame
from sys import exit


def handle_events(me) -> None:
    """обработка нажатий на клавиши"""
    for event in pygame.event.get():
        if event == pygame.QUIT:
            exit()


def update_screen(screen: pygame.Surface, screen_color: tuple, me) -> None:
    """прорисовка всех персонажей, карты, заднего фона"""
    screen.fill(screen_color)
    me.draw_character()
    pygame.display.flip()
