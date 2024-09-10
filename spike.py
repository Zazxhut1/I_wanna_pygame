import pygame

class Shu(pygame.sprite.Sprite):

    def __init__(self,image,point):

        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = point[0]
        self.rect.y = point[1]

class Heng(pygame.sprite.Sprite):

    def __init__(self,image,point):

        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = point[0]
        self.rect.y = point[1]

class Zhong(pygame.sprite.Sprite):

    def __init__(self,image,point):

        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = point[0]
        self.rect.y = point[1]