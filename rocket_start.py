import pygame

import rocket_func as func
from rocket import Rocket
from rocket_set import Settings


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((
        settings.screen_width, settings.screen_height))
    pygame.display.set_caption('My Rocket')

    rocket = Rocket(settings, screen)

    while True:
        func.check_events(rocket)
        rocket.update()
        func.update_screen(settings, screen, rocket)


run_game()
