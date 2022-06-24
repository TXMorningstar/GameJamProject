import sys
from typing import Union

import pygame
from pygame.surface import SurfaceType

import sprite
import toolkit
from data import gameConst
import tools.card as cardTools


# 点击牌组事件
def clickCardSet(e: pygame.event.Event):
    if gameConst.cardSet.rect.collidepoint(e.pos[0], e.pos[1]):
        if len(cardTools.playerCards.sprites()) < 5:
            card = sprite.CapitalCard("image/launch.png", "image/launch_big.png", (1750, 820))
            cardTools.playerCards.add(card)


# 事件字典
# 字典内容: eventName: Function[]
eventDict = {
    pygame.MOUSEBUTTONDOWN: [clickCardSet]
}


# 启动事件监听
def startEventListening():
    for event in pygame.event.get():
        if event.type in eventDict:
            for eventFunc in eventDict[event.type]:
                eventFunc(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def entrance(scn: Union[pygame.Surface, SurfaceType]):
    logo = pygame.image.load(toolkit.res_path("image/GAMExFAMILY_BANNER.png")).convert_alpha()
    for i in range(255):
        logo.set_alpha(i)
        scn.blit(logo, (0, 0))
        pygame.time.Clock().tick(120)
        pygame.display.flip()