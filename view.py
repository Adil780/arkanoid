import pygame, model, settings, os
os.environ["SDL_VIDEODRIVER"] = "directx"
pygame.init()

screen = pygame.display.set_mode([settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT])

def draw():

    screen.fill([0, 255, 0])
    pygame.draw.rect(screen, [255, 0, 0], model.platform)
    pygame.draw.circle(screen, [0, 0, 255], [model.ball.centerx, model.ball.centery], model.ball.width // 2)
    #pygame.draw.rect(screen, [0, 0, 0], model.ball, 2)
    for i in model.blocks:
        pygame.draw.rect(screen, [240, 50, 60], i)
    pygame.display.flip()