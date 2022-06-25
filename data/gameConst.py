import sprite
import pygame

# 游戏内固定组件
# 牌组
capitalCardSet = sprite.CardSet("capital", (1750, 820))
bureaucratCardSet = sprite.CardSet("bureaucrat", (1780, 57), is_horizontal=True)

workerCardSet = sprite.CardSet("bureaucrat", (1780, 57), is_horizontal=True)

cardSets = pygame.sprite.Group()
cardSets.add(capitalCardSet)
# cardSets.add(bureaucratCardSet)
cardSets.add(workerCardSet)

