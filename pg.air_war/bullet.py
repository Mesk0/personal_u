import pygame
from pygame.sprite import Sprite

# 继承pygame中的Sprite类
class Bullet(Sprite):
    # 通过思考不同对象之间的联系，导入相关实参
    def __init__(self, ai_settings, screen, ship):
        super().__init__()
        self.screen = screen
        # 子弹不基于图像，所以使用pygame.Rect方法在（0， 0）位置创建矩形
        # 子弹形状控制
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        # 子弹参数设置导入
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    # 控制子弹位置函数
    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y

    # 在屏幕上绘制子弹函数
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)








