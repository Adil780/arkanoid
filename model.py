import pygame, settings

platform = pygame.Rect(550, 720, 170, 20)
platform.centerx = settings.SCREEN_WIDTH / 2

blocks = []
for l in range(3, 5):
    for i in range(0, settings.SCREEN_WIDTH, 50):
        block = pygame.Rect(i, l * 50, 49, 49)
        blocks.append(block)

ball = pygame.Rect(600, 500, 50, 50)
ball.centerx = settings.SCREEN_WIDTH / 2
ball.centery = settings.SCREEN_HEIGHT / 2

speedx = 5
speedy = 5

def move_platform_to(posx):
    platform.centerx = posx
    if platform.right >= settings.SCREEN_WIDTH:
        platform.right = settings.SCREEN_WIDTH
    if platform.left <= 0:
        platform.left = 0

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
        speedx = -10
    if ball.left <= 0:
        ball.left = 0
        speedx = 10

    ball.y += speedy
    if ball.top <= 0:
        ball.top = 0
        speedy = 10
    if ball.bottom >= settings.SCREEN_HEIGHT:
        ball.bottom = settings.SCREEN_HEIGHT
        speedy = -10

    if ball.colliderect(platform):
        ball.bottom = platform.top
        speedy = -10



    p = ball.collidelistall(blocks)
    p.sort(reverse=True)
    for b in p:
        if ball.top <= blocks[b].bottom:
            speedy = 10
        del blocks[b]



