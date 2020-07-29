import pygame
from settings import Setting
from character import Character
from game_functions import handle_events, update_screen


def main():
    setting = Setting()
    pygame.init()
    screen = pygame.display.set_mode((setting.screen_width, setting.screen_height))
    me = Character(screen)
    pygame.display.set_caption('MORTAL ARENA')
    while True:
        handle_events(me)
        update_screen(screen, setting.screen_color, me)


if __name__ == '__main__':
    main()
