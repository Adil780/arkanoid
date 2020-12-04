import pygame, settings

platform = pygame.Rect(550, 720, 170, 20)
platform.centerx = settings.SCREEN_WIDTH / 2


def move_platform_right():
    platform.x += 5
    if platform.right >= settings.SCREEN_WIDTH:
        platform.right = settings.SCREEN_WIDTH


def move_platform_left():
    platform.x -= 5
    if platform.left <= 0:
        platform.left = 0


def step():
    pass
