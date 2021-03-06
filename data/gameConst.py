import sprite
import pygame

# 游戏内固定组件
# 牌组
workerCardSet = sprite.CardSet("worker", (1780, 820))
capitalCardSet = sprite.CardSet("capital", (1750, 57), is_horizontal=True)  # 传入is_horizontal参数可以让卡横着放

button = sprite.Button()
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
    "capital": ["_996", "escape", "launch", "fire", "investment", "cell", "promote", "propose", "humanresource"],
    "brueaucrat": ["landing", "notregret", "advantage"],
    "worker": ["bbq", "rest", "strike", "judge", "groupmsg", "highspace", "makeunion", "giveup"]
}


