import sys
import pygame


def check_keydown_events(event, rocket):
    """Реагує на натискання клавіш."""
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = True
    if event.key == pygame.K_LEFT:
        rocket.moving_left = True
    if event.key == pygame.K_UP:
        rocket.moving_up = True
    if event.key == pygame.K_DOWN:
        rocket.moving_down = True
    # elif event.key == pygame.K_q:
    #     sys.exit()


def check_keyup_events(event, rocket):
    """Реагує на відпускання клавіш."""
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = False
    if event.key == pygame.K_LEFT:
        rocket.moving_left = False
    if event.key == pygame.K_UP:
        rocket.moving_up = False
    if event.key == pygame.K_DOWN:
        rocket.moving_down = False


def check_events(rocket):
    """Обробляє натискання клавіатури та події миші"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, rocket)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, rocket)


def update_screen(settings, screen, rocket):
    """Оновлює зображення на екрані та відображає новий екран"""
    screen.fill(settings.bg_color)
    rocket.blitme()
    pygame.display.flip()
