import sys
import pygame
import toolkit as tk
import sprite as sp


pygame.init()
screen = pygame.display.set_mode((1000,1000))

p = sp.Player("image/GAMExFAMILY.png", (500,500), anchor = "center")

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
    screen.blit(p.image, p.rect)


    pygame.time.Clock().tick(30)
    pygame.display.flip()
