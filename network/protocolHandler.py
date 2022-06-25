import random

from data import gameConst
from tools import logger


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

        upperClass = gameConst.playerClass[0]
        lowerClass = gameConst.playerClass[1]

        # 发放身份
        player1Class = random.choice(gameConst.playerClass)
        player2Class = gameConst.playerClass[0]
        if player1Class == upperClass:
            player2Class = lowerClass

        print(player1Class)
        print(player2Class)

        server.role = player1Class
        # 向客户端发送身份
        server.send({
            "protocol": "srv_role_random",
            "data": player2Class
        })

        logger.log("随机抽选身份成功, 本局身份" + ("上级阶层" if server.role == upperClass else "下级阶层"))

    @staticmethod
    def srv_connect(client, protocol: dict):
        client.connectState = True
        logger.log("服务端连接成功")

    @staticmethod
    def srv_role_random(client, protocol: dict):
        upperClass = gameConst.playerClass[0]
        client.role = protocol["data"]
        logger.log("随机抽选身份成功, 本局身份" + "上级阶层" if client.role == upperClass else "下级阶层")

    @staticmethod
    def deal_card():
        pass
