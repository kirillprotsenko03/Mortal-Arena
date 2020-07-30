import pygame
from sys import exit


def handle_events(character) -> None:
    """обработка нажатий на клавиши"""
    for event in pygame.event.get():
        if event == pygame.QUIT:
            exit()
        _controlling_character_direction(event, character)
    character.move()


def update_screen(screen: pygame.Surface, screen_color: tuple, personage) -> None:
    """прорисовка всех персонажей, карты, заднего фона"""
    screen.fill(screen_color)
    personage.draw()
    pygame.display.flip()


def _controlling_character_direction(event: pygame.event, character) -> None:
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            character.change_direction(1, 0)
        elif event.key == pygame.K_LEFT:
            character.change_direction(-1, 0)
        elif event.key == pygame.K_UP:
            character.change_direction(0, -1)
        elif event.key == pygame.K_DOWN:
            character.change_direction(0, 1)
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            character.change_direction(0, 0)


