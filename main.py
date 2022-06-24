import sys
import pygame
import toolkit as tk
import sprite as sp


pygame.init()
screen = pygame.display.set_mode((1920,1080))

board = sp.Board("image/board.jpg", (0, 0))
card = sp.CapitalCard("image/launch.png", "image/launch_big.png", (433, 806))

GAME_IS_ON = True
while GAME_IS_ON:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            # p.rect.center = event.pos
            pass

    screen.fill(tk.black)
    board.draw(screen)
    card.draw(screen,False)


    pygame.time.Clock().tick(60)
    pygame.display.flip()
