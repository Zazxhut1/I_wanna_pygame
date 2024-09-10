import pygame

def check_img(kid,tops,tick,kid_r,kid_l,walk_r,walk_l,jump_r,jump_l):
    result = pygame.sprite.spritecollide(kid,tops,False)
    if result:
        kid.rect.y = result[0].rect.y - 20
        kid.yspeed = 0
        kid.jump = 2
        if kid.xspeed > 0 and tick > 4:
            return walk_r
        elif kid.xspeed < 0 and tick > 4:
            return walk_l
        else:
            if kid.faceleft:
                return kid_l
            else:
                return kid_r
    else:
        if kid.faceleft:
            return jump_l
        else:
            return jump_r

def check_a(kid,bottoms,lefts,rights):
    result0 = pygame.sprite.spritecollide(kid,bottoms,False)
    result1 = pygame.sprite.spritecollide(kid,lefts,False)
    result2 = pygame.sprite.spritecollide(kid,rights,False)
    if result0:
        kid.yspeed = 0
        kid.rect.y = result0[0].rect.y + 16
    if result1:
        kid.rect.x -= 1
    if result2:
        kid.rect.x += 1

def check_save(bullets,saves,saved):
    saving = pygame.sprite.groupcollide(bullets,saves,True,True)
    if saving:
        saved += 1
        return saved
    else:
        return saved

def check_death(kid,spikes):
    death = pygame.sprite.spritecollide(kid,spikes,False)
    return death

def check_win(kid,win):
    if_win = pygame.sprite.collide_rect(kid,win)
    return if_win