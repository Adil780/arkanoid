import pygame, time
from pygame import display as dis, event
pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

screen = dis.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

while True:
    time.sleep(1)
    t = event.get()
    for i in t:
        if i.type == pygame.QUIT:
            exit()