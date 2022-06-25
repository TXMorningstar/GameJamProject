import socket

import pygame

import toolkit as tk
import sprite as sp
import font.font as f

import tools.card as cardTools
from data import gameConst, gameValue
import tools.function as funcTools
from network.client import Client
from network.server import Server


screen = pygame.display.set_mode((1920, 1080))
board = sp.Board("image/board.png", (0, 0))

funcTools.entrance(screen)

choose = input("======多人游戏======\n1. 创建房间\n2. 加入房间\n直接输入ip地址可直接加入房间\n输入 1/2/ip 开始游戏\n")
if choose == "1":
    port = input("======房间创建======\n输入房间端口(默认25566)\n")
    if port == "":
        port = 25566
    gameValue.socket = Server(socket.gethostbyname(socket.gethostname()), port)
elif choose == "2":
    address = input("======加入房间======\n输入房间地址(ip:端口)\n")
    addressList = address.split(":")
    gameValue.socket = Client(addressList[0], int(addressList[1]))
elif ":" in choose:
    addressList = choose.split(":")
    gameValue.socket = Client(addressList[0], int(addressList[1]))



GAME_IS_ON = True
while GAME_IS_ON:
    funcTools.startEventListening()

    screen.fill(tk.black)
    board.draw(screen)

    # 显示玩家持有卡牌
    cardTools.drawPlayerCards(screen)

    # 牌组显示
    gameConst.workerCardSet.draw(screen)
    gameConst.capitalCardSet.draw(screen)

    f.draw_upper_info(screen)
    f.draw_lower_info(screen)


    pygame.display.flip()
