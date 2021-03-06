import os
import sys


# 游戏路径相关 ##############################################
def res_path(relative_path):
    gameFolder = os.path.dirname(os.path.realpath(sys.argv[0]))
    return "%s\%s" % (gameFolder, relative_path)


# 定义一些常用颜色 ##########################################
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


def my_turn(turn, playerRole):
    if playerRole in ["capital", "bureaucrat"]:
        # 如果回合为奇数，角色为上层
        if turn % 2 != 0:
            return True
        else:
            return False
    elif playerRole in ["worker", "union", "new_capital"]:
        if turn % 2 == 0:
            return True
        else:
            return False