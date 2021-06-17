import pygame
from pygame import *

class Window:
    def __init__(self, cellsize, height, width):
        self.cellsize = cellsize
        self.height = height
        self.width = width

        self.surface = pygame.display.set_mode((cellsize*width,cellsize*height))

    def draw(self,battlefield):
        self.surface.fill((0,0,150))
        battlefield.updateField()
        field = battlefield.field

        for i in range(self.height-1):
            print(i)
            for j in range(self.width-1):
                print(j)
                if field[j][i] == 'S':
                    dot = pygame.Rect(self.cellsize*j,self.cellsize*i,self.cellsize,self.cellsize)
                    pygame.draw.rect(self.surface,(125,125,125),dot)
                elif field[j][i] == 'M':
                    dot = pygame.Rect(self.cellsize*j,self.cellsize*i,self.cellsize,self.cellsize)
                    pygame.draw.rect(self.surface,(255,0,0),dot)
        

        for i in range(self.height):
            pygame.draw.line(self.surface,(0,0,0),(0,i*self.cellsize),(self.width*self.cellsize,i*self.cellsize))
        for i in range(self.width):
            pygame.draw.line(self.surface,(0,0,0),(i*self.cellsize,0),(i*self.cellsize,self.height*self.cellsize))


        pygame.display.update()