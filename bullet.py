import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self,face,x,y,screen):

        super().__init__()

        if face:
            self.speed = -10
        else:
            self.speed = 10
        self.image = pygame.image.load('./texture/bullet.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y + 9
        self.screen = screen

    def blitme(self):
        self.rect.x += self.speed
        self.screen.blit(self.image,(self.rect.x,self.rect.y))

    def check(self):
        if self.rect.x < 0 or self.rect.x > 750:
            return True
        else:
            return False