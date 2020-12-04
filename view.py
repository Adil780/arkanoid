import pygame, model, settings
pygame.init()
screen = pygame.display.set_mode([settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT])

def draw():

    screen.fill([0, 255, 0])
    pygame.draw.rect(screen, [255, 0, 0], model.platform)
    pygame.display.flip()