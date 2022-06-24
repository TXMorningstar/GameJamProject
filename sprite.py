import pygame
import toolkit as tk

class Sprite(pygame.sprite.Sprite):
    def __init__(self, image_path:str, position:tuple, anchor:str="topleft") -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(tk.res_path(image_path))
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.__setRect(anchor,position)

    def __setRect(self,anchor,position):
        if anchor == "top":
            self.rect.top = position
        elif anchor == "bottom":
            self.rect.bottom = position
        elif anchor == "left":
            self.rect.left = position
        elif anchor == "right":
            self.rect.right = position
        elif anchor == "topleft":
            self.rect.left = position
        elif anchor == "topright":
            self.rect.topright = position
        elif anchor == "bottomleft":
            self.rect.bottomleft = position
        elif anchor == "bottomright":
            self.rect.bottomright = position
        elif anchor == "midtop":
            self.rect.midtop = position
        elif anchor == "midbottom":
            self.rect.midbottom = position
        elif anchor == "midleft":
            self.rect.midleft = position
        elif anchor == "midright":
            self.rect.midright = position
        elif anchor == "center":
            self.rect.center = position


# 使用键盘移动，按下键后持续向某个特定方向移动
class PlayerKey(Sprite):
    def __init__(self, images_path: list, position: tuple, speed: int = 0, anchor: str = "topleft") -> None:
        super().__init__(images_path[0], position, anchor)
        self.animation_set = images_path
        self.present_ani_frame = 0
        self.speed = 0
        self.motion = list()
        self.direction = {
            "up": (0, -self.speed),
            "down": (0, self.speed),
            "left": (-self.speed, 0),
            "right": (self.speed, 0)
        }

    def setMotion(self, args):
        self.motion.insert(0, args)
    
    def update(self, mode, args):
        if mode == "move":
            self.move(args)
        elif mode == "animate":
            self.animate()
        elif mode == "collide":
            self.collideTest(args)

    def move(self, args):
        """Reset"""
        x, y = self.rect.topleft
        dx, dy = 0, 0

        for motion in self.motion:
            dx, dy = self.direction["direction"]
            x += dx
            y += dy
        self.motion.remove(motion)
        self.__setRect((x, y))


    def animate(self):
        """Update Player's Animation"""
        self.present_ani_frame += 1
        self.image = pygame.image.load(self.animation_set[self.present_ani_frame])

    def collideTest(self, args):
        pass


# 使用键盘控制，每次按下固定距离的玩家对象，用于阻塞式游戏
class PlayerClick(Sprite):
    def __init__(self, images_path: list, position: tuple, speed: int = 0, anchor: str = "topleft") -> None:
        super().__init__(images_path[0], position, anchor)
        self.animation_set = images_path
        self.present_ani_frame = 0
        self.speed = 0

    def update(self, mode, args=None):
        if mode == "move":
            self.setMotion(args)
        elif mode == "animate":
            self.animate(args)
        elif mode == "collide":
            self.collideTest(args)
    
    def setMotion(self, args) -> None:
        """Set Player's New Position"""
        pass

    def animate(self):
        """Update Player's Animation"""
        self.present_ani_frame += 1
        self.image = pygame.image.load(self.animation_set[self.present_ani_frame])

    def collideTest(self, args):
        pass


# 使用鼠标控制的玩家对象
class PlayerMouse(Sprite):
    def __init__(self, images_path: list, position: tuple, anchor: str = "topleft") -> None:
        super().__init__(images_path[0], position, anchor)
        self.animation_set = images_path
        self.present_ani_frame = 0

    def update(self, mode, args):
        if mode == "move":
            self.setMotion(args)
        elif mode == "animate":
            self.animate(args)
        elif mode == "collide":
            self.collideTest(args)

    def move(self, pos):
        self.rect.center = pos

    def animate(self):
        """Update Player's Animation"""
        self.present_ani_frame += 1
        self.image = pygame.image.load(
        self.animation_set[self.present_ani_frame])
    
    def collideTest(self, args):
        pass
