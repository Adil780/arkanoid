import pygame, model
pygame.init()
pygame.key.set_repeat(10)
def control():
    t = pygame.event.get()

    for i in t:
        if i.type == pygame.QUIT:
            exit()

        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_RIGHT:
                model.move_platform_right()
            if i.key == pygame.K_LEFT:
                model.move_platform_left()


