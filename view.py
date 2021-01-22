import pygame, model, settings, os
os.environ["SDL_VIDEODRIVER"] = "directx"
pygame.init()

letters = pygame.font.match_font("arial", True, False)
print(letters)

f = pygame.font.Font(letters, 20)
h = pygame.font.Font(letters, 100)

screen = pygame.display.set_mode([settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT])

last_lives = None



def change_text():
    global liwes, last_lives
    if model.lives != last_lives:
        liwes = f.render("LIVES = " + str(model.lives), True, [0, 0, 255])
        last_lives = model.lives
def game_over():
    global gmov
    if model.lives < 0:
        screen.fill([0, 0, 0])
        gmov = h.render("GAME OVER", True, [255, 255, 255])
        gw = gmov.get_width()
        gh = gmov.get_height()
        rect = pygame.Rect(50, 50, gw, gh)
        rect.center = [settings.SCREEN_WIDTH / 2, settings.SCREEN_HEIGHT / 2]
        screen.blit(gmov, rect)








def draw():
    change_text()
    screen.fill([0, 255, 0])
    pygame.draw.rect(screen, [255, 0, 0], model.platform)
    #pygame.draw.rect(screen, [0, 0, 0], model.ball, 2)
    for i in model.blocks:
        pygame.draw.rect(screen, [255, 0, 230], i)
    pygame.draw.circle(screen, [0, 0, 255], [model.ball.centerx, model.ball.centery], model.ball.width // 2)
    screen.blit(liwes, [1050, 750])
    game_over()
    pygame.display.flip()
