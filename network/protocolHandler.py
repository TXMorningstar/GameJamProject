import random
import sprite
from data import gameConst, gameValue
from tools import logger

import tools.card as cardTools
from tools.function import card_group


class ProtocolHandler:
    def __call__(self, obj, protocol: dict):
        protocolName = protocol['protocol']
        if not hasattr(self, protocolName):
            return
        function = getattr(self, protocolName)
        result = function(obj, protocol)
        return result

    @staticmethod
    def cli_connect(server, protocol: dict):
        server.send({"protocol": "srv_connect"})
        server.connectState = True
        logger.log("客户端连接成功")

        capital = gameConst.playerClass[0]
        worker = gameConst.playerClass[1]

        # 发放身份
        player1Role = random.choice(gameConst.playerClass)
        player2Role = gameConst.playerClass[0]
        if player1Role == capital:
            player2Role = worker

        server.role = player1Role
        # 向客户端发送身份
        server.send({
            "protocol": "srv_role_random",
            "data": {
                "player1": server.role,
                "player2": player2Role
            }
        })

        gameValue.myPlayerRole = server.role
        gameValue.anotherPlayerRole = player2Role

        logger.log("随机抽选身份成功, 本局身份" + ("上级阶层" if server.role == capital else "下级阶层"))

    @staticmethod
    def srv_connect(client, protocol: dict):
        client.connectState = True
        logger.log("服务端连接成功")

    @staticmethod
    def srv_role_random(client, protocol: dict):
        capital = gameConst.playerClass[0]
        client.role = protocol["data"]["player2"]

        gameValue.anotherPlayerRole = protocol["data"]["player1"]
        gameValue.myPlayerRole = client.role

        logger.log("随机抽选身份成功, 本局身份" + ("上级阶层" if client.role == capital else "下级阶层"))

    @staticmethod
    def deal_card(socket, protocol: dict):
        data = protocol["data"]

        if data["role"] not in ["capital", "bureaucrat"]:
            card = sprite.Worker(data["card_name"], (1750, 820))
            card.isBack = True
            cardTools.lowerPlayerCards.add(card)
        else:
            if data["card_type"] == "capital":
                card = sprite.CapitalCard(data["card_name"], (1750, -200))
            else:
                card = sprite.BureaucratCard(data["card_name"], (1750, -200))
            card.isBack = True
            card.rect.x = 396 + (len(cardTools.upperPlayerCards.sprites()) * 210)
            cardTools.upperPlayerCards.add(card)

    @staticmethod
    def use_card(socket, protocol: dict):
        cardIndex = protocol["data"]["index"]
        card_group[gameValue.anotherPlayerRole].sprites()[cardIndex].use()

    @staticmethod
    def click_button(socket, protocol: dict):
        gameConst.button.pressed()
