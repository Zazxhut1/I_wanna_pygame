import pygame

class Kid(pygame.sprite.Sprite):

    def __init__(self,image,xspeed,yspeed,yaccele,point,screen):

        super().__init__()
        
        self.image = image
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.yaccele = yaccele
        self.rect = self.image.get_rect()
        self.rect.x = point[0]
        self.rect.y = point[1]
        self.screen = screen
        self.faceleft = False
        self.jump = 2

    def speed_change(self):
        self.yspeed += self.yaccele

    def update(self,*args):
        self.rect.x += self.xspeed
        self.rect.y += self.yspeed

    def face_update(self):
        if self.xspeed < 0:
            self.faceleft = True
        elif self.xspeed > 0:
            self.faceleft = False

    def blitme(self,image):
        self.screen.blit(image,(self.rect.x,self.rect.y))