import pygame
from sys import exit

from bullet import Bullet

def key(kid,screen,bullets,sound_s,sound_j):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                kid.xspeed += 1
            elif event.key == pygame.K_LEFT:
                kid.xspeed -= 1
            elif event.key == pygame.K_LSHIFT:
                if kid.jump > 0:
                    kid.yspeed = -5
                    kid.jump -= 1
                    sound_j.play()
            elif event.key == pygame.K_z:
                newbullet = Bullet(kid.faceleft,kid.rect.x,kid.rect.y,screen)
                bullets.add(newbullet)
                sound_s.play()
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
            elif event.key == pygame.QUIT:
                pygame.quit()
                exit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                kid.xspeed -= 1
            elif event.key == pygame.K_LEFT:
                kid.xspeed += 1