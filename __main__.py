import pygame, time, view, controller, model
pygame.init()


while True:
    time.sleep(1/60)

    controller.control()

    model.step()

    view.draw()