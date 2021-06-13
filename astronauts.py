import pygame, sys
from SimpleDrawEngine import *


class Player(pygame.sprite.Sprite):
    def __init__(self, screen, imagem, rect, angle, pos_x):
        super(Player, self).__init__()
        self.screen = screen
        self.original_image = pygame.image.load(imagem).convert_alpha()
        self.angle = angle
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = 300 - self.rect.height / 2


    def move(self, speed):
        # self.pos_x += 1
        self.rect.x += speed
        

    def animation(self, angle):
        ## scaling the image
        self.original_image = pygame.transform.scale(self.original_image, (150, 150)) 
        self.image = pygame.transform.rotate(self.original_image, angle)
        angle %= 360
        x, y = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        # self.rect = self.image.get_rect()
        # self.rect.center = (self.rect.x, 300)
        # old_center = self.rect.center
        # new_image = self.image = pygame.transform.rotate(self.image, angle)
        # self.rect = new_image.get_rect()
        # self.rect.center = old_center
        
        self.screen.blit(self.image, self.rect)

