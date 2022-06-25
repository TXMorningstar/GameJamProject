import json
import socket
from threading import Thread

from network.protocolHandler import ProtocolHandler
from tools import logger


class Client:

    def __init__(self, ip: str, port: int):
        self.socket = socket.socket()
        self.connectState = False
        self.protocolHandle = ProtocolHandler()
        self.role = None

        thread = Thread(target=self.connect, args=(ip, port))
        thread.setDaemon(True)
        thread.start()

    def connect(self, ip: str, port: int):
        try:
            self.socket.connect((ip, port))
            self.send({"protocol": "cli_connect"})
            self.receiveMessage()
        except ConnectionRefusedError:
            logger.log("无法连接服务器")

    def receiveMessage(self):
        data = self.socket.recv(4096)
        strPackage = data.decode("utf-8")
        packages = strPackage.split("|#|")
        for jsonPackage in packages[:-1]:
            package = json.loads(jsonPackage)
            self.protocolHandle(self, package)

    def send(self, data: dict):
        self.socket.sendall((json.dumps(data, ensure_ascii=False)+"|#|").encode())


