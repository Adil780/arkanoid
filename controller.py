import pygame, model, settings
pygame.init()
pygame.key.set_repeat(1)
pygame.mouse.set_visible(False)
def control():
    t = pygame.event.get()

    for i in t:
        if i.type == pygame.QUIT:
            exit()

        if i.type == pygame.MOUSEMOTION:
            a = i.pos[0]
            model.move_platform_to(a)

        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_RIGHT:
                model.move_platform_right()
            if i.key == pygame.K_LEFT:
                model.move_platform_left()



