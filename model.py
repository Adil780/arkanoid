import pygame, settings

platform = pygame.Rect(550, 720, 170, 20)
platform.centerx = settings.SCREEN_WIDTH / 2

ball = pygame.Rect(600, 500, 50, 50)
ball.centerx = settings.SCREEN_WIDTH / 2
ball.centery = settings.SCREEN_HEIGHT / 2

speedx = 5
speedy = 5

def move_platform_right():
    platform.x += 5
    if platform.right >= settings.SCREEN_WIDTH:
        platform.right = settings.SCREEN_WIDTH


def move_platform_left():
    platform.x -= 5
    if platform.left <= 0:
        platform.left = 0


def step():
    global speedx, speedy
    ball.x += speedx


    if ball.right >= settings.SCREEN_WIDTH:
        ball.right = settings.SCREEN_WIDTH
        speedx = -5
    if ball.left <= 0:
        ball.left = 0
        speedx = 5

    ball.y += speedy
    if ball.top <= 0:
        ball.top = 0
        speedy = 5
    if ball.bottom >= settings.SCREEN_HEIGHT:
        ball.bottom = settings.SCREEN_HEIGHT
        speedy = -5

