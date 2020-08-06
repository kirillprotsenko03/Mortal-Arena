import pygame
from sys import exit


def handle_events(character) -> None:
    """обработка нажатий на клавиши"""
    for event in pygame.event.get():
        if event == pygame.QUIT:
            exit()
        _controlling_character_direction(event, character)
    character.move()


def update_screen(screen: pygame.Surface, screen_color: tuple, personage, m) -> None:
    """прорисовка всех персонажей, карты, заднего фона"""
    screen.fill(screen_color)
    personage.draw()
    m.draw()
    pygame.display.flip()


def is_collision(first_obj, second_obj) -> bool:
    """проверка соприкосновения объектов"""
    if first_obj.height < second_obj.height:
        first_obj, second_obj = second_obj, first_obj
    first_rect_min_x = first_obj.x
    first_rect_min_y = first_obj.y
    first_rect_max_x = first_obj.right
    first_rect_max_y = first_obj.bottom
    second_rect_min_x = second_obj.x
    second_rect_min_y = second_obj.y
    second_rect_max_x = second_obj.right
    second_rect_max_y = second_obj.bottom

    if first_rect_min_x <= second_rect_min_x <= first_rect_max_x and first_rect_min_y <= second_rect_min_y <= first_rect_max_y:
        return True
    elif first_rect_min_x <= second_rect_max_x <= first_rect_max_x and first_rect_min_y <= second_rect_min_y <= first_rect_max_y:
        return True
    elif first_rect_min_x <= second_rect_min_x <= first_rect_max_x and first_rect_min_y <= second_rect_max_y <= first_rect_max_y:
        return True
    elif first_rect_min_x <= second_rect_max_x <= first_rect_max_x and first_rect_min_y <= second_rect_max_y <= first_rect_max_y:
        return True
    return False



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
