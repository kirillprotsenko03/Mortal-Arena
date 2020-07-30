import pygame
from settings import Setting
from character import Character
from game_functions import handle_events, update_screen


def main():
    clock = pygame.time.Clock()
    setting = Setting()
    pygame.init()
    screen = pygame.display.set_mode((setting.screen_width, setting.screen_height))
    personage = Character(screen, setting)
    pygame.display.set_caption('MORTAL ARENA')
    while True:
        clock.tick(60)
        handle_events(personage)
        update_screen(screen, setting.screen_color, personage)


if __name__ == '__main__':
    main()
