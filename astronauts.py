import pygame, sys
from SimpleDrawEngine import *

pos_x = -360
vx = 10
class Player:
    def __init__(self, screen, imagem, rect, angle):
        
        self.screen = screen
        self.imagem = pygame.image.load(imagem).convert()
        self.rect = rect
        self.angle = angle

    def animation(self):
        global pos_x, vx
        ## scaling the image
        self.imagem = pygame.transform.scale(self.imagem, (150, 150))
        ## 
        self.rect = self.imagem.get_rect()
        self.rect.center = (pos_x, 300)
        old_center = self.rect.center
        new_image = self.imagem = pygame.transform.rotate(self.imagem, self.angle)
        self.rect = new_image.get_rect()
        self.rect.center = old_center
        pos_x += vx
        vx -= 0.035
        if vx <= 0:
            vx = 0
        self.screen.blit(self.imagem, self.rect)
