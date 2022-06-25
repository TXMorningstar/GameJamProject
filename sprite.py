import pygame
import toolkit as tk


class Board(pygame.sprite.Sprite):
    """背景的精灵"""

    def __init__(self, main_board, position: tuple) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.main_board = pygame.image.load(tk.res_path(main_board))
        self.rect = self.main_board.get_rect()
        self.rect.topleft = position

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.main_board, self.rect)


# 代发的卡牌组
class CardSet(pygame.sprite.Sprite):
    def __init__(self, job: str, position: tuple, is_horizontal: bool = False) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.job = job

        if not is_horizontal:
            self.card_back = pygame.image.load(tk.res_path("image/%s_card_back.png" % job))
        else:
            self.card_back = pygame.image.load(tk.res_path("image/%s_card_back_horizontal.png" % job))

        self.rect = self.card_back.get_rect()
        self.rect.midtop = position

    def draw(self, screen):
        """绘制的时候先绘制插画再绘制"""
        screen.blit(self.card_back, self.rect)


class Cards(pygame.sprite.Sprite):
    def __init__(self, illustration, illustration_big, card_front, card_back, card_front_big, card_back_big, position: tuple) -> None:
        pygame.sprite.Sprite.__init__(self)
        # 创建图片的surface对象，illustration是卡牌上的插画，front是卡牌正面，back是卡背，big后缀是大号的卡牌
        self.illustration = pygame.image.load(tk.res_path(illustration))
        self.illustration_big = pygame.image.load(
            tk.res_path(illustration_big))
        self.card_front = pygame.image.load(
            tk.res_path(card_front))
        self.card_front_big = pygame.image.load(
            tk.res_path(card_front_big))
        self.card_back = pygame.image.load(
            tk.res_path(card_back))
        self.card_back_big = pygame.image.load(
            tk.res_path(card_back_big))

        self.rect = self.card_front.get_rect()
        self.rect.midtop = position
        self.rect_big = self.card_front_big.get_rect()
        self.rect_big.midbottom = self.rect.midtop

        self.is_big = False

    def update(self):
        """用于group的调用"""
        pass

    def draw(self, screen):
        """绘制的时候先绘制插画再绘制牌框，big参数为True时绘制大的卡牌，否则绘制小号的"""
        if not self.is_big:
            screen.blit(self.illustration, self.rect)
            screen.blit(self.card_front, self.rect)
        else:
            screen.blit(self.illustration_big, self.rect_big)
            screen.blit(self.card_front_big, self.rect_big)


class CapitalCard(Cards):
    """资本家的卡牌"""
    def __init__(self, card_name: str, position: tuple) -> None:
        # 创建图片的surface对象，illustration是卡牌上的插画，front是卡牌正面，back是卡背，big后缀是大号的卡牌
        # 只用传入card_name即可，然后根据cardname自动寻找对应的卡面图案
        super().__init__("image/%s.png" % card_name, "image/%s_big.png" % card_name, "image/capital_card_front.png",
                         "image/capital_card_back.png", "image/capital_card_front_big.png", "image/capital_card_back_big.png", position)
        
        self.name = card_name
        self.card_function = {
            "escape": self.escape,
            "996": self._996
        }

    def update(self):
        """用于group的调用"""
        pass

    def use(self):
        self.card_function["card_name"]()

    def escape(self):
        print("escape used")

    def _996(self):
        pass


class BureaucratCard(Cards):
    """官僚的卡牌"""

    def __init__(self, card_name, position: tuple) -> None:
        # 创建图片的surface对象，illustration是卡牌上的插画，front是卡牌正面，back是卡背，big后缀是大号的卡牌
        super().__init__("image/%s.png" % card_name, "image/%s_big.png" % card_name, "image/capital_card_front.png",
                         "image/capital_card_back.png", "image/capital_card_front_big.png", "image/capital_card_back_big.png", position)

        self.name = card_name
        self.card_function = {
            
        }

    def update(self):
        """用于group的调用"""
        pass


class Worker(Cards):
    def __init__(self, card_name, position: tuple) -> None:
        # 创建图片的surface对象，illustration是卡牌上的插画，front是卡牌正面，back是卡背，big后缀是大号的卡牌
        super().__init__("image/%s.png" % card_name, "image/%s_big.png" % card_name, "image/worker_card_front.png",
                         "image/worker_card_back.png", "image/worker_card_front_big.png", "image/worker_card_back_big.png", position)

        self.name = card_name
        self.card_function = {
            "bbq": self.bbq
        }


    def update(self):
        pass


    def bbq(self):
        pass

