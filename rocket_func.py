import sys
import pygame


def _check_keydown_events(event, rocket):
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

def _check_events(self):
    """Обробляє натискання клавіатури та події миші"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            self._check_keydown_events(event)
        elif event.type == pygame.KEYUP:
            self._check_keyup_events(event)





def _check_keyup_events(self, event):
    """Реагує на відпускання клавіш."""
    if event.key == pygame.K_RIGHT:
        self.rocket.moving_right = False
    elif event.key == pygame.K_LEFT:
        self.rocket.moving_left = False
    elif event.key == pygame.K_UP:
        self.rocket.moving_height = False
    elif event.key == pygame.K_DOWN:
        self.rocket.moving_width = False


def _update_screen(self):
    """Оновлює зображення на екрані та відображає новий екран"""
    self.screen.fill(self.settings.bg_color)
    self.rocket.blitme()

    pygame.display.flip()
