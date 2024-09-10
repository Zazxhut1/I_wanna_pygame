import pygame

class Top(pygame.sprite.Sprite):

    def __init__(self,screen,point,image):

        super().__init__()
        
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = point[0]
        self.rect.y = point[1]
        self.screen = screen

    def blitme(self):
        self.screen.blit(self.image,(self.rect.x,self.rect.y))

class Bottom(pygame.sprite.Sprite):

    def __init__(self,screen,point,image):

        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = point[0]
        self.rect.y = point[1]
        self.screen = screen

    def blitme(self):
        self.screen.blit(self.image,(self.rect.x,self.rect.y))

class Left(pygame.sprite.Sprite):

    def __init__(self,screen,point,image):

        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = point[0]
        self.rect.y = point[1]
        self.screen = screen

    def blitme(self):
        self.screen.blit(self.image,(self.rect.x,self.rect.y))

class Right(pygame.sprite.Sprite):

    def __init__(self,screen,point,image):

        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = point[0]
        self.rect.y = point[1]
        self.screen = screen

    def blitme(self):
        self.screen.blit(self.image,(self.rect.x,self.rect.y))

class Save(pygame.sprite.Sprite):

    def __init__(self,screen,point,image):

        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = point[0]
        self.rect.y = point[1]
        self.screen = screen

    def blitme(self):
        self.screen.blit(self.image,(self.rect.x,self.rect.y))

class Spike():

    def __init__(self,screen,point,image):
        self.image = image[point[2]]
        self.x = point[0]
        self.y = point[1]
        self.screen = screen

    def blitme(self):
        self.screen.blit(self.image,(self.x,self.y))

class Edge():

    def __init__(self,screen,point,image):
        self.image = image
        self.x = point[0]
        self.y = point[1]
        self.screen = screen

    def blitme(self):
        self.screen.blit(self.image,(self.x,self.y))

class Saved():

    def __init__(self,screen,point,image):
        self.image = image
        self.x = point[0]
        self.y = point[1]
        self.screen = screen

    def blitme(self):
        self.screen.blit(self.image,(self.x,self.y))

class Ghost():

    def __init__(self,screen,image):
        self.image = image
        self.screen = screen

    def blitme(self,kid):
        self.screen.blit(self.image,(kid.rect.x,kid.rect.y))

class Win(pygame.sprite.Sprite):

    def __init__(self,screen,point,image):

        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = point[0]
        self.rect.y = point[1]
        self.screen = screen

    def blitme(self):
        self.screen.blit(self.image,(self.rect.x,self.rect.y))