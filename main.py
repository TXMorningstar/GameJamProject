import socket

import pygame

import toolkit as tk
import sprite as sp
import font.font as f

import tools.card as cardTools
import data.gameConst as gc
import data.gameValue as gv
import tools.function as funcTools
from network.client import Client
from network.server import Server

screen = pygame.display.set_mode((1920, 1080))
board = sp.Board("image/board.png", (0, 0))

funcTools.entrance(screen)
pygame.mixer.music.load("sounds/bgm.wav")
pygame.mixer.music.play()

choose = input("======多人游戏======\n1. 创建房间\n2. 加入房间\n直接输入ip地址可直接加入房间\n输入 1/2/ip 开始游戏\n")
if choose == "1":
    port = input("======房间创建======\n输入房间端口(默认25566)\n")
    if port == "":
        port = 25566
    gv.socket = Server(socket.gethostbyname(socket.gethostname()), int(port))
elif choose == "2":
    address = input("======加入房间======\n输入房间地址(ip:端口)\n")
    addressList = address.split(":")
    gv.socket = Client(addressList[0], int(addressList[1]))
elif ":" in choose:
    addressList = choose.split(":")
    gv.socket = Client(addressList[0], int(addressList[1]))



# 游戏流程
def playing():
    funcTools.startEventListening() 

    screen.fill(tk.black)
    board.draw(screen)

    # 文字显示
    f.draw_lower_info(screen)
    f.draw_upper_info(screen)

    # 按钮显示
    gc.button.draw(screen)

    # 牌组显示
    gc.workerCardSet.draw(screen)
    gc.capitalCardSet.draw(screen)

    # 显示玩家持有卡牌
    cardTools.drawPlayerCards(screen)

# 游戏结束
def end():
    screen.fill(tk.black)

    if gv.WINNER == "capital":
        text = f.upperPlayerFont.render("上层玩家获得了胜利", True, tk.white)
        screen.blit(text, (800,800))
    elif gv.WINNER == "worker":
        text = f.lowerPlayerFont.render("下层玩家获得了胜利", True, tk.white)
        screen.blit(text, (800, 800))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()


game_state = {
    "playing": playing,
    "end": end
}



GAME_IS_ON = True
while GAME_IS_ON:
    print(gv.TURN)
    game_state[gv.GAME_STATE]()

    pygame.display.flip()
