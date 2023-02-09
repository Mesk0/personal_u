import sys
import pygame
from bullet import Bullet
from alien import Alien
# 导入sleep()实现游戏暂停
from time import sleep


# 处理游戏中键盘操作事件函数
def check_event(ai_settings, screen, stats, play_button, ship, aliens, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # mouse.get.pos()返回一个元组，记录鼠标点击时的x、y坐标
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y)

# 检查鼠标是否位于按钮rect内
def check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    # collidepoint()检查鼠标单击位置是否在按钮的rect内
    # 重置游戏
    if button_clicked and play_button.rect.collidepoint(mouse_x, mouse_y):
        # 重置游戏速度
        ai_settings.initialize_dynamic_settings()
        # 游戏开始时，隐藏光标
        pygame.mouse.set_visible(False)
        stats.game_active = True
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

# 处理键盘放开事件函数
def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

# 处理键盘按下事件函数（调用飞船相关函数，调用子弹相关函数）
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    # 子弹射击函数调用
    elif event.key == pygame.K_SPACE:
        # 判定子弹数量是否处于允许数量内
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

# 子弹射击函数
def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

# 删除子弹函数
def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    bullets.update()
    # 循环内存在删除元素时，直接按照本体数量遍历容易出错，所以按照副本遍历
    # 删除已消失的子弹
    for bullet in bullets.copy():
        # 判定子弹已经超出顶部
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)

# 删除发生碰撞的子弹和外星人
def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(collisions.keys())
            sb.prep_score()
    # 外星人群为空时，删除所有子弹，并创建新的外星人群
    if len(aliens) == 0:
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens)

# 屏幕刷新函数
def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    screen.fill(ai_settings.bg_color)
    # 绘制所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    # Sprite类绘制时用Draw()
    aliens.draw(screen)
    sb.show_score()
    # 如果游戏处于非活动状态，绘制play按钮
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()

# 计算每行外星人数量
def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    # 使用int确保数量为整数
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

# 创建一个外星人（类）
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

# 计算外星人群行数
def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

# 创建外星人群
def create_fleet(ai_settings,  screen, ship, aliens):
    # 创建一个外星人，计算一行能容纳外星人的数量
    alien = Alien(ai_settings, screen)
    # 调用函数，计算每行可容纳的外星人数量
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    # 按照rows逐行创建外星人群
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # 每次循环创建一个外星人（类）
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

# 检测是否有外星人触及屏幕边缘函数&下移外星人函数
def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

# 移动外星人群的方向函数
def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

# 飞船与外星人碰撞时发生的函数
def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    # 减小游戏次数，并清空子弹、外星人
    if stats.ships_left > 0:
        stats.ships_left -= 1
        aliens.empty()
        bullets.empty()
        # 创建新外星人群
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

# 飞船与屏幕底部碰撞的发生的函数
def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break

# 外星人群位置更新函数
def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    # 检测飞船与外星人碰撞情况
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)





