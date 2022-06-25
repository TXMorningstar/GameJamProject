import sprite
import pygame

# 游戏内固定组件
# 牌组
capitalCardSet = sprite.CardSet("capital", (1750, 57), is_horizontal=True)  # 传入is_horizontal参数可以让卡横着放
bureaucratCardSet = sprite.CardSet("bureaucrat", (1780, 57), is_horizontal=True)

workerCardSet = sprite.CardSet("worker", (1780, 820))

# 用group管理牌组
cardSets = pygame.sprite.Group()
cardSets.add(capitalCardSet)
# cardSets.add(bureaucratCardSet)
cardSets.add(workerCardSet)

