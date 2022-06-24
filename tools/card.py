from typing import Union

import pygame

# 玩家卡牌
from pygame.surface import SurfaceType

playerCards = pygame.sprite.Group()


# 绘制玩家卡牌
def drawPlayerCards(screen: Union[pygame.Surface, SurfaceType]):
    for i in range(len(playerCards.sprites())):
        cardSprite = playerCards.sprites()[i]
        if i == 0:
            cardSprite.minX = 400
        else:
            cardSprite.minX = playerCards.sprites()[i - 1].rect.x + 220

        if cardSprite.rect.x > cardSprite.minX:
            cardSprite.rect.x -= 30
        screen.blit(cardSprite.illustration, cardSprite.rect)
        screen.blit(cardSprite.card_front, cardSprite.rect)
