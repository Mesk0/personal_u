import pygame.image


class Ship():
    # 设置ship的默认属性
    def __init__(self, ai_settings,screen):
        # 导入screen,以便对ship与screen的相对位置进行操作
        self.screen = screen
        # 导入游戏设置飞行参数
        self.ai_settings = ai_settings
        # 导入飞船图片
        self.image = pygame.image.load('image/ship.bmp')
        # 获取导入图片的rect形状，并赋给ship的rect形状
        self.rect = self.image.get_rect()
        # 获取screen的形状
        self.screen_rect = screen.get_rect()
        # 使ship位于screen的底部中央位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # 浮点数记录飞船的x的坐标
        self.center = float(self.rect.centerx)
        # ship左右移动的初始移动参数
        self.moving_right = False
        self.moving_left = False

    # 设置ship的移动条件
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    # 在self.rect位置绘制self.image到屏幕上
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx

