from typing import Union

import pygame

# 玩家卡牌
from pygame.surface import SurfaceType

import toolkit

lowerPlayerCards = pygame.sprite.Group()
upperPlayerCards = pygame.sprite.Group()


# 绘制玩家卡牌，同时卡牌会向左移动
def drawPlayerCards(screen: Union[pygame.Surface, SurfaceType]):
    drawUpperPlayerCards(screen)
    drawLowerPlayerCards(screen)


# 绘制下层玩家的卡牌
def drawLowerPlayerCards(screen: Union[pygame.Surface, SurfaceType]):
    for i in range(len(lowerPlayerCards.sprites())):
        cardSprite = lowerPlayerCards.sprites()[i]
        if i == 0:
            cardSprite.minX = 400
        else:
            cardSprite.minX = lowerPlayerCards.sprites()[i - 1].rect.x + 220

        if cardSprite.rect.x > cardSprite.minX:
            cardSprite.rect.x -= 30
            cardSprite.rect_big.x -= 30

        cardSprite.draw(screen)


# 绘制上层玩家卡牌，同时卡牌会向下移动
def drawUpperPlayerCards(screen: Union[pygame.Surface, SurfaceType]):
    for i in range(len(upperPlayerCards.sprites())):
        cardSprite = upperPlayerCards.sprites()[i]
        # 设定x值
        if i == 0:
            cardSprite.minX = 400
        else:
            cardSprite.minX = upperPlayerCards.sprites()[i - 1].rect.x + 220

        cardSprite.rect.x = cardSprite.minX

        # 设定y值
        if cardSprite.rect.bottom < 265:
            cardSprite.rect.y += 5

        cardSprite.draw(screen)


def loadImageToSurface(path: str) -> pygame.Surface:
    return pygame.image.load(toolkit.res_path(path))
