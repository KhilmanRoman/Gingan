import pygame,sys
from bullet import Bullet
from ina import Ino
import time

def events(screen,gun, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                gun.mright = True
            elif event.key == pygame.K_a:
                gun.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                gun.mright = False
            elif event.key == pygame.K_a:
                gun.mleft = False

def update(bg_color, screen, gun, inas, bullets):
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    inas.draw(screen)
    pygame.display.flip()

def update_bullets(screen, inas, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, inas, True, True)
    if len(inas) == 0:
        bullets.empty()
        create_army(screen, inas)

def gun_kill(stats, screen, gun, inas, bullets):
    stats.guns_left -=1
    inas.empty()
    bullets.empty()
    create_army(screen, inas)
    gun.create_gun()
    time.sleep(1)

def update_inas(stats, screen, gun, inas, bullets):

    inas.update()
    if pygame.sprite.spritecollideany(gun,inas):
        gun_kill(stats, screen, gun, inas, bullets)
    inas_check(stats, screen, gun, inas, bullets)



def inas_check(stats, screen, gun, inas, bullets):
    screen_rect = screen.get_rect()
    for ina in inas.sprites():
        if ina.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, gun, inas, bullets)
            break

def create_army(screen, inas):
    ina = Ino(screen)
    ina_width = ina.rect.width
    number_ina_x = int((700 - 2 * ina_width) / ina_width)
    ina_height = ina.rect.height
    number_ina_y = int((800 - 500 - 2 * ina_height) / ina_height)

    for row_number in range(number_ina_y):
        for ina_number in range(number_ina_x):
            ina = Ino(screen)
            ina.x = ina_width + (ina_width * ina_number)
            ina.y = ina_height + (ina_height * row_number)
            ina.rect.x = ina.x
            ina.rect.y = ina.rect.height + (ina.rect.height * row_number)
            inas.add(ina)


