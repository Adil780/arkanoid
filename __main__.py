import pygame, time
from pygame import display as dis, event
pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

screen = dis.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

platform = pygame.Rect(550, 720, 170, 20)
platform.centerx = SCREEN_WIDTH / 2

pygame.key.set_repeat(10)

while True:
    time.sleep(1/60)

    #CONTROLLER
    t = event.get()
    for i in t:
        if i.type == pygame.QUIT:
            exit()

        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_RIGHT:
                platform.x += 5
            if i.key == pygame.K_LEFT:
                platform.x -= 5

    #MODEL
    if platform.right >= SCREEN_WIDTH:
        platform.right = SCREEN_WIDTH

    if platform.left <= 0:
        platform.left = 0








    #VIEW
    screen.fill([0, 255, 0])
    pygame.draw.rect(screen, [255, 0, 0], platform)
    dis.flip()