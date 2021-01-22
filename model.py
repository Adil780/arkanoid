import pygame, settings
pygame.init()
platform = pygame.Rect(550, 720, 170, 20)
platform.centerx = settings.SCREEN_WIDTH / 2

lives = 5
state = "stop"

blocks = []

for l in range(0, 5):
    for i in range(0, settings.SCREEN_WIDTH, settings.BLOCK_SIZE):
        block = pygame.Rect(i, l * settings.BLOCK_SIZE, settings.BLOCK_SIZE - 1, settings.BLOCK_SIZE - 1)
        blocks.append(block)

ball = pygame.Rect(100, 600, 40, 40)
ball.centerx = settings.SCREEN_WIDTH / 2
ball.centery = settings.SCREEN_HEIGHT / 2

speedx = 0
speedy = 0


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
    global speedx, speedy, lives

    ball.x += speedx

    if ball.right >= settings.SCREEN_WIDTH:
        ball.right = settings.SCREEN_WIDTH
        speedx = -10
    if ball.left <= 0:
        ball.left = 0
        speedx = 10

    p = ball.collidelistall(blocks)
    p.sort(reverse=True)
    for b in p:
        if ball.colliderect(blocks[b]):
            if speedx < 0:
                ball.left = blocks[b].right
            elif speedx > 0:
                ball.right = blocks[b].left
            del blocks[b]
    if len(p) > 0:
        speedx = -speedx

    ball.y += speedy

    if ball.top <= 0:
        ball.top = 0
        speedy = 10
    if ball.bottom >= settings.SCREEN_HEIGHT:
        ball.bottom = settings.SCREEN_HEIGHT
        speedy = -10

    a = platform.centerx
    second_part = platform.left + platform.width / 4
    third_part = a
    forth_part = platform.right - platform.width / 4

    if ball.colliderect(platform):
        b = ball.centerx
        if b < second_part:
            speedx = -10
            speedy = -3

        elif b >= second_part and b < third_part:
            speedx = -9
            speedy = -6

        elif b >= a and b < forth_part:
            speedx = 9
            speedy = -6

        elif b >= forth_part:
            speedx = 10
            speedy = -3



        ball.bottom = platform.top
    p = ball.collidelistall(blocks)
    p.sort(reverse=True)
    for b in p:
        if ball.colliderect(blocks[b]):
            if speedy < 0:
                ball.top = blocks[b].bottom
            elif speedy > 0:
                ball.bottom = blocks[b].top
            del blocks[b]
    if len(p) > 0:
        speedy = -speedy

def lost_live():
    global lives, speedy, speedx, state
    if ball.bottom >= settings.SCREEN_HEIGHT:
        ball.center = [settings.SCREEN_WIDTH / 2, settings.SCREEN_HEIGHT / 2]
        lives -= 1
        speedy = 0
        speedx = 0
        state = "stop"
        print(lives)

def play_match():
    global speedx, speedy, state
    if state == "stop":
        speedy = 10
        speedx = 10
        state = "play"