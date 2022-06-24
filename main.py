import sys
import pygame
import toolkit as tk
import sprite as sp

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
board = sp.Board("image/board.png", (0, 0))

# 游戏内组件
# 牌组
cardSet = sp.CardSet((1750, 820))

# 玩家卡牌
cards = pygame.sprite.Group()

# 变量
# 拿牌
TAKING_CARD = False


# 事件
def entrance(scn):
    logo = pygame.image.load(tk.res_path("image/GAMExFAMILY_BANNER.png")).convert_alpha()
    for i in range(255):
        logo.set_alpha(i)
        scn.blit(logo, (0, 0))
        pygame.time.Clock().tick(120)
        pygame.display.flip()


# 点击牌组事件
def clickCardSet(e: pygame.event.Event):
    if cardSet.rect.collidepoint(e.pos[0], e.pos[1]):
        if len(cards.sprites()) < 5:
            card = sp.CapitalCard("image/launch.png", "image/launch_big.png", (1750, 820))
            cards.add(card)


# 事件字典
# 字典内容: eventName: Function[]
eventDict = {
    pygame.MOUSEBUTTONDOWN: [clickCardSet]
}
# entrance(screen)

GAME_IS_ON = True
while GAME_IS_ON:
    for event in pygame.event.get():
        if event.type in eventDict:
            for eventFunc in eventDict[event.type]:
                eventFunc(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(tk.black)
    board.draw(screen)

    # 牌组显示
    cardSet.draw(screen, False)

    # 绘制玩家卡牌
    for i in range(len(cards.sprites())):
        cardSprite = cards.sprites()[i]
        if i == 0:
            cardSprite.minX = 400
        else:
            cardSprite.minX = cards.sprites()[i - 1].rect.x + 220

        if cardSprite.rect.x > cardSprite.minX:
            cardSprite.rect.x -= 30
        screen.blit(cardSprite.illustration, cardSprite.rect)
        screen.blit(cardSprite.card_front, cardSprite.rect)

    pygame.time.Clock().tick(60)
    pygame.display.flip()
