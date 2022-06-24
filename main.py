import sys
import pygame
import toolkit as tk
import sprite as sp

import tools.card as cardTools
from data import gameConst
import tools.function as funcTools

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
board = sp.Board("image/board.png", (0, 0))

funcTools.entrance(screen)

GAME_IS_ON = True
while GAME_IS_ON:

    funcTools.startEventListening()

    screen.fill(tk.black)
    board.draw(screen)

    # 牌组显示
    gameConst.cardSet.draw(screen, False)

    # 显示玩家持有卡牌
    cardTools.drawPlayerCards(screen)

    pygame.time.Clock().tick(60)
    pygame.display.flip()
