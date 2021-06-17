import pygame
from pygame import *
import os

class Sprite(pygame.sprite.Sprite):
    def __init__(self,path,cellsize):
        super().__init__()
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, 'Sprites')

        self.image = pygame.image.load(os.path.join(img_folder, path)).convert()
        self.image = pygame.transform.smoothscale(self.image,(cellsize,cellsize))
        self.rect = self.image.get_rect()

    def move(self,pos_x,pos_y):
        self.rect.x = pos_x
        self.rect.y = pos_y

    def turn(self, angle):
        self.image = pygame.transform.rotate(self.image, angle)