import pygame, sys
from SimpleDrawEngine import *


class Player:
    def __init__(self, screen, imagem, rect, angle, pos_x):
        
        self.screen = screen
        self.imagem = pygame.image.load(imagem).convert_alpha()
        self.rect = rect
        self.angle = angle
        self.pos_x = pos_x

    def animation(self):
        ## scaling the image
        self.imagem = pygame.transform.scale(self.imagem, (150, 150))

        self.rect = self.imagem.get_rect()
        self.rect.center = (self.pos_x, 300)
        old_center = self.rect.center
        new_image = self.imagem = pygame.transform.rotate(self.imagem, self.angle)
        self.rect = new_image.get_rect()
        self.rect.center = old_center
        
        self.screen.blit(self.imagem, self.rect)

