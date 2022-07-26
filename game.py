import pygame, controls
from gun import Gun
from pygame.sprite import Group
from stats import Stats


def run():
    pygame.init()
    screen = pygame.display.set_mode((700,600))
    pygame.display.set_caption("Cosmic")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    inas = Group()
    controls.create_army(screen, inas)
    stats = Stats()

    while True:
        controls.events(screen, gun, bullets)
        gun.update_gun()
        controls.update(bg_color, screen, gun, inas, bullets)
        controls.update_bullets(screen, inas, bullets)
        controls.update_inas(stats, screen, gun, inas, bullets)

run()