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

playerClass = [
    "upper_class",
    "lower_class"
]

# 所有职业与对应卡牌
card_decks = {
    "capital": ["996", "escape", "launch"],
    "brueaucrat": [],
    "worker": ["bbq", "rest", "strike"]
}

# 重要全局变量 ##########################################
# 资本家部分
MARKET_VALUE = 1  # 市值，以百万为单位结算
WORKERS = 10  # 工人数量

# 官僚部分
TRACE = 0

# 工人部分 ##########################################
DISSATISFACTION = 0  # 不满值
RELATION = 0  # 人脉
