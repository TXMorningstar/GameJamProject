import pygame
import toolkit as tk


class Board(pygame.sprite.Sprite):
    def __init__(self, main_board, position: tuple) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.main_board = pygame.image.load(tk.res_path(main_board))
        self.rect = self.main_board.get_rect()
        self.rect.topleft = position

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.main_board, self.rect)


class CapitalCard(pygame.sprite.Sprite):
    def __init__(self, illustration, illustration_big, position: tuple) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.illustration = pygame.image.load(tk.res_path(illustration))
        self.illustration_big = pygame.image.load(tk.res_path(illustration_big))
        self.card_front = pygame.image.load(tk.res_path("image/capital_card_front.png"))
        self.card_front_big = pygame.image.load(tk.res_path("image/capital_card_front_big.png"))
        self.card_back = pygame.image.load(tk.res_path("image/capital_card_back.png"))
        self.card_back_big = pygame.image.load(tk.res_path("image/capital_card_back_big.png"))

        self.rect = self.card_front.get_rect()
        self.rect.midTop = position
        self.rect_big = self.card_front_big.get_rect()
        self.rect_big.midBottom = position

    def update(self):
        pass

    def draw(self, screen, big=False):
        """绘制的时候先绘制插画再绘制"""
        if not big:
            screen.blit(self.illustration, self.rect)
            screen.blit(self.card_front, self.rect)
        else:
            screen.blit(self.illustration_big, self.rect.midtop)
            screen.blit(self.card_front_big, self.rect.midtop)


class Bureaucrat(pygame.sprite.Sprite):
    def __init__(self, illustration, illustration_big, position) -> None:
        pygame.sprite.Sprite.__init__(self)
        
        self.illustration = pygame.image.load(tk.res_path(illustration))
        self.illustration_big = pygame.image.load(tk.res_path(illustration_big))
        self.card_front = pygame.image.load(tk.res_path("image/bureaucrat_card_front.png"))
        self.card_front_big = pygame.image.load(tk.res_path("image/bureaucrat_card_front_big.png"))
        self.card_back = pygame.image.load(tk.res_path("image/bureaucrat_card_back.png"))
        self.card_back_big = pygame.image.load(tk.res_path("image/bureaucrat_card_back_big.png"))

        self.rect = self.card_front.get_rect()
        self.rect.midTop = position
        self.rect_big = self.card_front_big.get_rect()
        self.rect_big.midBottom = position
