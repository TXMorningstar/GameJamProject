import sys
from typing import Union

import pygame
from pygame.surface import SurfaceType
import random

import sprite
import toolkit as tk
from data import gameConst, gameValue
import tools.card as cardTools


def get_random_card(job):
    return random.choice(gameConst.card_decks[job])


card_type = {
    "capital": sprite.CapitalCard,
    "bureaucrat": sprite.BureaucratCard,
    "worker": sprite.Worker,
}

card_group = {
    "capital": cardTools.upperPlayerCards,
    "bureaucrat": cardTools.upperPlayerCards,

    "worker": cardTools.lowerPlayerCards,
}



# 点击牌组事件，添加新的卡牌
def clickCardSet(e: pygame.event.Event):
    # 卡牌碰撞
    for cardSet in gameConst.cardSets:
        if cardSet.rect.collidepoint(e.pos[0], e.pos[1]):
            if gameValue.myPlayerRole == cardSet.job:
                if gameValue.myPlayerRole not in ["capital", "bureaucrat"]:
                    if len(cardTools.lowerPlayerCards.sprites()) < 5:
                        card_name = get_random_card(cardSet.job)
                        card = card_type[cardSet.job](card_name, (1750, 820))
                        cardTools.lowerPlayerCards.add(card)
                        gameValue.socket.send({
                            "protocol": "deal_card",
                            "data": {
                                "role": gameValue.myPlayerRole
                            }
                        })
                else:
                    if len(cardTools.upperPlayerCards.sprites()) < 5:
                        card_name = get_random_card(cardSet.job)
                        card = card_type[cardSet.job](card_name, (1750, -200))
                        card.rect.x = 396 + \
                            (len(cardTools.upperPlayerCards.sprites()) * 210)
                        cardTools.upperPlayerCards.add(card)
                        gameValue.socket.send({
                            "protocol": "deal_card",
                            "data": {
                                "role": gameValue.myPlayerRole
                            }
                        })


# 点击卡牌出牌，然后调用相应的功能
def clickCard(e: pygame.event.Event):
    # 找到自己身份对应的，遍历其中的卡牌
    try:
        for card in card_group[gameValue.myPlayerRole].sprites():
            if card.rect.collidepoint(e.pos[0], e.pos[1]):
                if e.button == 1:
                    card.use()
                    data = {
                        "protocol": "use_card",
                        "data": {
                            "name": card.name
                        }
                    }
                    gameValue.socket.send(data)
    except Exception as ret:
        print("error:", ret)


# 鼠标滑过卡牌事件
def cardHover(e: pygame.event.Event):
    for card in cardTools.lowerPlayerCards:
        if card.rect.collidepoint(e.pos[0], e.pos[1]):
            # 如果鼠标与当前卡牌发生碰撞，就切换卡牌显示
            card.is_big = True
        else:
            # 如果鼠标与当前卡牌没有发生碰撞，就切换回小卡片
            card.is_big = False


def quit_game(event):
    if event.key == pygame.K_ESCAPE:
        pygame.quit()
        sys.exit()

# 事件字典
# 字典内容: eventName: Function[]
eventDict = {
    pygame.MOUSEBUTTONDOWN: [clickCardSet, clickCard],
    pygame.MOUSEMOTION: [cardHover],
    pygame.KEYDOWN: [quit_game]
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
    logo = pygame.image.load(tk.res_path("image/GAMExFAMILY_BANNER.png")).convert_alpha()
    for i in range(128 * 3):
        # 渐入
        if i < 128:
            logo.set_alpha(i * 2)
        # 渐出
        elif i > 128 * 2:
            logo.set_alpha(128 * 3 - i)
        scn.fill(tk.black)
        scn.blit(logo, (0, 0))
        pygame.display.flip()


# 这个入场更快，测试的时候覆盖掉上面的正式入场
def entrance(scn):
    logo = pygame.image.load(tk.res_path("image/GAMExFAMILY_BANNER.png")).convert_alpha()
    for i in range(5):
        scn.blit(logo, (0, 0))
        pygame.time.Clock().tick(60)
        pygame.display.flip()
