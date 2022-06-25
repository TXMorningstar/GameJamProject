import sprite
import pygame

# 游戏内固定组件
# 牌组
workerCardSet = sprite.CardSet("worker", (1780, 820))
capitalCardSet = sprite.CardSet("capital", (1750, 57), is_horizontal=True)  # 传入is_horizontal参数可以让卡横着放

# bureaucratCardSet = sprite.CardSet("bureaucrat", (1780, 57), is_horizontal=True)

# 用group管理牌组
cardSets = pygame.sprite.Group()
cardSets.add(workerCardSet)
cardSets.add(capitalCardSet)

playerClass = [
    "capital",
    "worker"
]

# 所有职业与对应卡牌
card_decks = {
    "capital": ["996", "escape", "launch", "culture", "fire"],
    "brueaucrat": ["landing"],
    "worker": ["bbq", "rest", "strike"]
}