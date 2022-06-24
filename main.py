import sys
import pygame
import toolkit as tk
import sprite as sp


def entrance(scn):
    logo = pygame.image.load(tk.res_path("image/GAMExFAMILY_BANNER.png")).convert_alpha()
    for i in range(255):
        logo.set_alpha(i)
        scn.blit(logo, (0, 0))
        pygame.time.Clock().tick(120)
        pygame.display.flip()


pygame.init()
screen = pygame.display.set_mode((1920, 1080))
board = sp.Board("image/board.png", (0, 0))
card = sp.CapitalCard("image/launch.png", "image/launch_big.png", (433, 806))

entrance(screen)

GAME_IS_ON = True
while GAME_IS_ON:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            pass

    screen.fill(tk.black)
    board.draw(screen)
    card.draw(screen, False)

    pygame.time.Clock().tick(60)
    pygame.display.flip()
