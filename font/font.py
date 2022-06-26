import pygame
import data.gameValue as gv
import toolkit as tk

pygame.init()
pygame.font.init()

upperPlayerFont = pygame.font.Font(tk.res_path("font/TsangerYuMo.ttf"), 40)
lowerPlayerFont = pygame.font.Font(tk.res_path("font/TsangerYuMo.ttf"), 40)

cardNameFont = pygame.font.Font(tk.res_path("font/华康新综艺W7.TTF"), 20)
cardDiscriptionFont = pygame.font.Font(
    tk.res_path("font/SourceHanSerifCN.otf"), 10)

cardNameFont_big = pygame.font.Font(tk.res_path("font/华康新综艺W7.TTF"), 40)
cardDiscriptionFont_big = pygame.font.Font(
    tk.res_path("font/SourceHanSerifCN.otf"), 20)


def draw_upper_info(screen):
    content = "市值: %s亿" % gv.MARKET_VALUE
    content2 = "员工: %s人" % gv.WORKERS
    text = upperPlayerFont.render(content, True, tk.white)
    text2 = upperPlayerFont.render(content2, True, tk.white)
    screen.blit(text, (1670, 320))
    screen.blit(text2, (1670, 370))


def draw_lower_info(screen):
    content = "人脉: %s人" % gv.RELATION
    content2 = "不满: %s" % gv.DISSATISFACTION
    text = lowerPlayerFont.render(content, True, tk.black)
    text2 = lowerPlayerFont.render(content2, True, tk.black)
    screen.blit(text, (1635, 580))
    screen.blit(text2, (1635, 630))
