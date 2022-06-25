from tools import logger


class ProtocolHandler:
    def __call__(self, obj, protocol: dict):
        protocol = protocol['protocol']
        if not hasattr(self, protocol):
            return
        function = getattr(self, protocol)
        result = function(obj, protocol)
        return result

    @staticmethod
    def cli_connect(server, protocol: dict):
        server.send({"protocol": "srv_connect"})
        server.connectState = True
        logger.log("客户端连接成功")

    @staticmethod
    def srv_connect(client, protocol: dict):
        client.connectState = True
        logger.log("服务端连接成功")

    @staticmethod
    def deal_card():
        pass
