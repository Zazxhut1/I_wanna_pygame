import pygame
from sys import exit

from kid import Kid
import keyboard
import room
import brick
import check

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((750,570))
pygame.display.set_caption('I Wanna Pygame')
clock = pygame.time.Clock()
start = False
background = pygame.image.load('./texture/background.png')
pygame.mixer.music.load('./sounds/bgm0.mp3')
pygame.mixer.music.play(-1,0)

while start == False:
    clock.tick(60)
    screen.blit(background,(0,0))
    screen.blit(pygame.image.load('./texture/start.png'),(0,0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LSHIFT:
                start = True
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
    pygame.display.flip()

kid_r = pygame.image.load('./texture/kid_r.png')
kid_l = pygame.image.load('./texture/kid_l.png')
walk_r = pygame.image.load('./texture/walk_r.png')
walk_l = pygame.image.load('./texture/walk_l.png')
jump_r = pygame.image.load('./texture/jump_r.png')
jump_l = pygame.image.load('./texture/jump_l.png')
top_img = pygame.image.load('./texture/top.png')
bottom_img = pygame.image.load('./texture/bottom.png')
left_img = pygame.image.load('./texture/left.png')
right_img = pygame.image.load('./texture/right.png')
save_img = pygame.image.load('./texture/save.png')
spike_f_img = (pygame.image.load('./texture/spike_u.png'),pygame.image.load('./texture/spike_d.png'),pygame.image.load('./texture/spike_l.png'),pygame.image.load('./texture/spike_r.png'))
edge_img = pygame.image.load('./texture/edge.png')
saved_img = pygame.image.load('./texture/saved.png')
shu_img = pygame.image.load('./texture/shu.png')
heng_img = pygame.image.load('./texture/heng.png')
zhong_img = pygame.image.load('./texture/zhong.png')
ghost_img = pygame.image.load('./texture/ghost.png')
win_img = pygame.image.load('./texture/win.png')
death_pic = pygame.image.load('./texture/over.png')
win_pic = pygame.image.load('./texture/last.png')
sound_s = pygame.mixer.Sound('./sounds/shoot.wav')
sound_j = pygame.mixer.Sound('./sounds/jump.wav')

bullets = pygame.sprite.Group()
tops = pygame.sprite.Group()
bottoms = pygame.sprite.Group()
lefts = pygame.sprite.Group()
rights = pygame.sprite.Group()
saves = pygame.sprite.Group()
spikes = pygame.sprite.Group()
fake_s = []

tops = room.top_init(screen,tops,top_img)
bottoms = room.bottom_init(screen,bottoms,bottom_img)
lefts = room.left_init(screen,lefts,left_img)
rights = room.right_init(screen,rights,right_img)
saves = room.save_init(screen,saves,save_img)
fake_s = room.fake_init(screen,fake_s,spike_f_img,edge_img,saved_img)
spikes = room.spike_init(spikes,shu_img,heng_img,zhong_img)

saved = 0
living = True
w = False
savepoint = room.saving()
win = brick.Win(screen,(675,345),win_img)

while True:
    pygame.mixer.music.stop()
    pygame.mixer.music.load('./sounds/bgm1.mp3')
    pygame.mixer.music.play(-1,0)
    tick = 0
    point = savepoint[saved]
    kid = Kid(kid_r,0,0,0.2,point,screen)

    while True:
        clock.tick(60)
        tick += 1
        screen.blit(background,(0,0))
        for top in tops:
            top.blitme()
        for bottom in bottoms:
            bottom.blitme()
        for left in lefts:
            left.blitme()
        for right in rights:
            right.blitme()
        for fake in fake_s:
            fake.blitme()
        for save in saves:
            save.blitme()
        win.blitme()
        kid.speed_change()
        keyboard.key(kid,screen,bullets,sound_s,sound_j)
        kid.face_update()
        kid.update()
        for bullet in bullets:
            bullet.blitme()
            if bullet.check():
                bullets.remove(bullet)
        saved = check.check_save(bullets,saves,saved)
        kid_img = check.check_img(kid,tops,tick,kid_r,kid_l,walk_r,walk_l,jump_r,jump_l)
        check.check_a(kid,bottoms,lefts,rights)
        if check.check_death(kid,spikes):
            ghost = brick.Ghost(screen,ghost_img)
            ghost.blitme(kid)
            screen.blit(death_pic,(0,0))
            del kid
            pygame.display.flip()
            pygame.mixer.music.stop()
            pygame.mixer.music.load('./sounds/death.mp3')
            pygame.mixer.music.play(1,0)
            while living:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            living = False
            living = True
            del ghost
            break
        else:
            kid.blitme(kid_img)
        if check.check_win(kid,win):
            del kid
            w = True
            break
        pygame.display.flip()
        if tick == 9:
            tick = 0
    if w:
        screen.blit(background,(0,0))
        screen.blit(win_pic,(0,0))
        pygame.display.flip()
        pygame.mixer.music.stop()
        pygame.mixer.music.load('./sounds/bgm0.mp3')
        pygame.mixer.music.play(-1,0)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()