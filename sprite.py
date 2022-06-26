import random
import pygame
import toolkit as tk
import data.gameValue as gv
import font.font as f
import tools.card as cardTool

# 格式：{
#    "card_name": [card_display_name, card_discription, [card_discription2, ...]]
# }
card_description = {
    "_996": ["福报", "市值+10,不满+10"],  # 完成
    "escape": ["战略转移", "直到下个回合,你的市值归零"],
    "launch": ["发射骨灰盒", "如果你有100亿市值,获得胜利"],  # 完成
    "culture": ["狼性文化", "对方下回合出的牌必须比你这", "回合出的多,否则下回合不能摸牌"],
    "fire": ["裁员", "员工-5,市值+20,不满+10"],  # 完成
    "bargain": ["意思意思", "市值-5,获得一张官僚卡"],
    "investment": ["长期投资", "市值-10,抽两张牌"],  # 完成
    "cell": ["校园招聘", "获得一些临时员工,三回合后解聘他们"],  # 完成
    "promote": ["破格提拔", "不满值每回合下降10", "【延时卡】"],
    "landing": ["平稳落地", "如果你已经使用了转移了10亿资产,获得胜利"],
    "notregret": ["下次还敢", "切换回资本家,留下贪污证据+1"],
    "advantage": ["职务便利", "消除己方延时生效区的卡牌"],  # 完成
    "bbq": ["大排档", "人脉+5"],  # 完成
    "rest": ["蓄势待发", "本回合不能使用卡牌,抽三张卡"],  # 完成
    "strike": ["老子不干了", "三回合后若不满值高于50,员工减半", "【延时卡】"],
    "judge": ["劳动仲裁", "三回合后,市值减少30"]
}


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


class Button(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(tk.res_path("image/button.png"))
        self.rect = self.image.get_rect()
        self.rect.topleft = (93, 497)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def pressed(self):
        print("PRESSED")
        gv.TURN += 1
        if gv.myPlayerRole in ["worker", "union", "new_cap"]:
            gv.lowerPlayerDraw = 5
            gv.lowerPlayerUsable_card = 99999
        elif gv.myPlayerRole in ["capital", "bureaucrat"]:
            gv.upperPlayerDraw = 5

        for i in range(len(gv.delayCards)):
            delayCard = gv.delayCards[i]
            targetRound = delayCard["target_round"]
            if gv.TURN == targetRound:
                func = delayCard["func"]
                args = delayCard["args"]
                func(args)
                gv.delayCards.pop(i)



# 代发的卡牌组
class CardSet(pygame.sprite.Sprite):
    def __init__(self, job: str, position: tuple, is_horizontal: bool = False) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.job = job
        self.isHorizontal = is_horizontal
        self.card_back = pygame.image.load(tk.res_path("image/%s_card_back.png" % self.job))
        self.card_back_big = pygame.image.load(tk.res_path("image/%s_card_back.png" % self.job))

        self.rect = self.card_back.get_rect()
        self.rect.midtop = position
        self.rect_big = self.card_back_big.get_rect()
        self.rect_big.midbottom = self.rect.midtop

    def draw(self, screen):
        if not self.isHorizontal:
            self.card_back = pygame.image.load(tk.res_path("image/%s_card_back.png" % self.job))
        else:
            self.card_back = pygame.image.load(tk.res_path("image/%s_card_back_horizontal.png" % self.job))
        """绘制的时候先绘制插画再绘制"""
        screen.blit(self.card_back, self.rect)


class Cards(pygame.sprite.Sprite):
    def __init__(self, illustration, illustration_big, card_front, card_back, card_front_big, card_back_big,
                 position: tuple) -> None:
        pygame.sprite.Sprite.__init__(self)
        # 创建图片的surface对象，illustration是卡牌上的插画，front是卡牌正面，back是卡背，big后缀是大号的卡牌
        self.illustrationPath = illustration
        self.illustrationBigPath = illustration_big
        self.cardFrontPath = card_front
        self.cardFrontBigPath = card_front_big
        self.cardBackPath = card_back
        self.cardBackBigPath = card_back_big

        self.illustration = pygame.image.load(tk.res_path(illustration))
        self.illustration_big = pygame.image.load(tk.res_path(illustration_big))
        self.card_front = pygame.image.load(tk.res_path(card_front))
        self.card_front_big = pygame.image.load(tk.res_path(card_front_big))
        self.card_back = pygame.image.load(tk.res_path(card_back))
        self.card_back_big = pygame.image.load(tk.res_path(card_back_big))

        self.name = ""
        self.type = ""

        self.rect = self.card_front.get_rect()
        self.rect.midtop = position
        self.rect_big = self.card_front_big.get_rect()
        self.rect_big.midbottom = self.rect.midtop

        self.is_big = False

        self.isBack = False

    def draw(self, screen):
        """绘制的时候先绘制插画再绘制牌框,big参数为True时绘制大的卡牌,否则绘制小号的"""
        if not self.isBack:
            if not self.is_big:
                # 绘制小卡面的卡图
                screen.blit(self.illustration, self.rect)
                screen.blit(self.card_front, self.rect)
                # 绘制小卡面的文本
                contents = card_description[self.name]
                x, y = self.rect.topleft
                for i in range(len(contents)):
                    if i == 0:
                        nameFont = f.cardNameFont.render(contents[i], True, tk.black)
                        screen.blit(nameFont, (x + 10, y + 165))
                    else:
                        discriptionFont = f.cardDiscriptionFont.render(contents[i], True, tk.black)
                        screen.blit(discriptionFont, (x + 10, y + 180 + (i * 10)))

            else:
                # 绘制大卡面的卡图
                screen.blit(self.illustration_big, self.rect_big)
                screen.blit(self.card_front_big, self.rect_big)
                # 绘制小卡面的文本
                contents = card_description[self.name]
                x, y = self.rect_big.topleft
                for i in range(len(contents)):
                    if i == 0:
                        nameFont = f.cardNameFont_big.render(
                            contents[i], True, tk.black)
                        screen.blit(nameFont, (x + 20, y + 330))
                    else:
                        discriptionFont = f.cardDiscriptionFont_big.render(
                            contents[i], True, tk.black)
                        screen.blit(discriptionFont, (x + 20, y + 360 + (i * 20)))

        else:
            screen.blit(self.card_back, self.rect)

    # 使用卡牌
    def use(self):
        if not hasattr(self, self.name):
            return
        func = getattr(self, self.name)
        result = func(self)
        self.kill()
        return result


class CapitalCard(Cards):
    """资本家的卡牌"""

    def __init__(self, card_name: str, position: tuple) -> None:
        # 创建图片的surface对象，illustration是卡牌上的插画，front是卡牌正面，back是卡背，big后缀是大号的卡牌
        # 只用传入card_name即可，然后根据cardname自动寻找对应的卡面图案
        super().__init__("image/%s.png" % card_name, "image/%s_big.png" % card_name, "image/capital_card_front.png",
                         "image/capital_card_back.png", "image/capital_card_front_big.png",
                         "image/capital_card_back_big.png", position)
        self.name = card_name
        self.type = "capital"

    @staticmethod
    def escape(card: pygame.sprite.Sprite):
        print("escape used")

    @staticmethod
    def _996(card: pygame.sprite.Sprite):
        print("996 used")
        gv.DISSATISFACTION += 10
        gv.MARKET_VALUE += 5

    @staticmethod
    def launch(card: pygame.sprite.Sprite):
        print("launch used")
        if gv.MARKET_VALUE > 100:
            gv.GAME_STATE = "end"
            gv.WINNER = "capital"

    @staticmethod
    def culture(card: pygame.sprite.Sprite):
        print("culture used")

    @staticmethod
    def fire(card: pygame.sprite.Sprite):
        print("use fire")
        if gv.WORKERS > 5:
            gv.DISSATISFACTION += 10
            gv.MARKET_VALUE += 20

    @staticmethod
    def bargain(card: pygame.sprite.Sprite):
        print("bargain")

    @staticmethod
    def investment(card: pygame.sprite.Sprite):
        print("investment")
        gv.MARKET_VALUE -= 10
        gv.upperPlayerDraw += 2

    @staticmethod
    def cell(card: pygame.sprite.Sprite):
        print("cell")
        gv.WORKERS += 30
        cardTool.addDelayCard(gv.TURN + 4, card.cell_func, card)

    @staticmethod
    def cell_func(card: pygame.sprite.Sprite):
        gv.WORKERS -= 30

    @staticmethod
    def promote(card: pygame.sprite.Sprite):
        print("promote")


class BureaucratCard(Cards):
    """官僚的卡牌"""

    def __init__(self, card_name, position: tuple) -> None:
        # 创建图片的surface对象，illustration是卡牌上的插画，front是卡牌正面，back是卡背，big后缀是大号的卡牌
        super().__init__("image/%s.png" % card_name, "image/%s_big.png" % card_name, "image/capital_card_front.png",
                         "image/capital_card_back.png", "image/capital_card_front_big.png",
                         "image/capital_card_back_big.png", position)

        self.name = card_name
        self.type = "bureaucrat"

    @staticmethod
    def landing(self, card: pygame.sprite.Sprite):
        pass

    @staticmethod
    def notregret(card: pygame.sprite.Sprite):
        pass

    @staticmethod
    def advantage(card: pygame.sprite.Sprite):
        print("advantage")
        gv.upperPlayerTimeCard = None


class Worker(Cards):
    def __init__(self, card_name, position: tuple) -> None:
        # 创建图片的surface对象，illustration是卡牌上的插画，front是卡牌正面，back是卡背，big后缀是大号的卡牌
        super().__init__("image/%s.png" % card_name, "image/%s_big.png" % card_name, "image/worker_card_front.png",
                         "image/worker_card_back.png", "image/worker_card_front_big.png",
                         "image/worker_card_back_big.png", position)

        self.name = card_name
        self.type = "worker"

    @staticmethod
    def bbq(card: pygame.sprite.Sprite):
        gv.RELATION += 5

    @staticmethod
    def rest(card: pygame.sprite.Sprite):
        print("rest")
        gv.lowerPlayerUsable_card = 0
        gv.lowerPlayerDraw += 3

    @staticmethod
    def strike(card: pygame.sprite.Sprite):
        pass

    @staticmethod
    def judge(card: pygame.sprite.Sprite):
        pass


class Timer(object):
    def __init__(self, turn, name) -> None:
        # 触发时机
        self.turn = turn
        self.name = name
        map = {

        }

    def test(self):
        pass
