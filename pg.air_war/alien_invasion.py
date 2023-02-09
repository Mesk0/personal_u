import pygame
from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
import game_functions as gf
from scoreboard import Scoreboard
# pygame.sprite.Group存储所有有效子弹
from pygame.sprite import Group


def run_game():
    # 初始化背景设置
    pygame.init()
    # 创建游戏设置类（页面、飞船移速、子弹设置）
    ai_settings = Settings()
    # 创建屏幕
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(ai_settings, screen, "Play")
    # 根据游戏内存在对象，分别对游戏内对象（飞船、子弹、外星人）创建类
    # 在循环外创建类，避免游戏循环时在创建类，拖慢游戏速度
    ship = Ship(ai_settings, screen)
    # 子弹和外星人都是多个对象，所以在主函数内不创建类，而是直接创建一个空编组
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # 创建游戏统计数据类
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    while True:
        # 通过收集按键事件，调用相关函数，对飞船、子弹控制
        gf.check_event(ai_settings, screen, stats, play_button, ship, aliens, bullets)
        if stats.game_active:
            # 更新飞船位置
            ship.update()
            # 由于导入了sprite中的group类，所以游戏中的多个子弹会同时运行update函数
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        # 刷新屏幕
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()

