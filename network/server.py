import json
import socket
from threading import Thread

from network.protocolHandler import ProtocolHandler
from tools import logger


class Server:

    def __init__(self, ip: str, port: int):
        self.connection = None
        self.connectState = False
        self.protocolHandle = ProtocolHandler()
        self.role = None
        logger.log("服务端启动中...")

        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.bind((ip, port))
            self.socket.listen(5)
        except socket.error:
            logger.log("服务端启动失败...")

        logger.log("服务端启动成功 "+ip+":"+str(port))

        # 等待客户端连接
        # 新县城
        thread = Thread(target=self.waitConnect)
        # 设置成守护线程
        thread.setDaemon(True)
        thread.start()

    def waitConnect(self):
        while True:
            client = self.socket.accept()
            self.connection = client

            thread = Thread(target=self.messageHandle())
            # 设置成守护线程
            thread.setDaemon(True)
            thread.start()

    def messageHandle(self):
        while True:
            data = self.connection[0].recv(4096)
            strPackage = data.decode("utf-8")
            packages = strPackage.split("|#|")
            print(packages)
            for jsonPackage in packages[:-1]:
                package = json.loads(jsonPackage)
                self.protocolHandle(self, package)

    def send(self, data: dict):
        self.connection[0].sendall((json.dumps(data, ensure_ascii=False)+"|#|").encode())
