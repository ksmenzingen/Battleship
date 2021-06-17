import pygame
from pygame import *
from pygame import sprite
from Sprite import *

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

        spritegroup = pygame.sprite.Group()

        for i in range(self.height):
            for j in range(self.width):
                dot = Sprite("sprite_waves_1.png",self.cellsize)
                dot.move(j*self.cellsize,i*self.cellsize)
                spritegroup.add(dot)

        for s in battlefield.ships:
                    if not s.alive:
                        top = Sprite("ship_top.png",self.cellsize)
                        top.move(s.coordinates[0][0]*self.cellsize,s.coordinates[0][1]*self.cellsize)
                        bottom = Sprite("ship_low.png",self.cellsize)
                        bottom.move(s.coordinates[-1][0]*self.cellsize,s.coordinates[-1][1]*self.cellsize)
                        if s.align == 'h':
                            top.turn(90)
                            bottom.turn(90)
                        spritegroup.add(bottom)
                        spritegroup.add(top)
                        for k in range(1,len(s.coordinates)-1):
                            middle = Sprite("ship_middle.png",self.cellsize)
                            middle.move(s.coordinates[k][0]*self.cellsize,s.coordinates[k][1]*self.cellsize)
                            if s.align == 'h':
                                middle.turn(90)
                            spritegroup.add(middle)

        spritegroup.draw(self.surface)

        for m in battlefield.missedShots:
            dot = pygame.Rect(self.cellsize*m[0],self.cellsize*m[1],self.cellsize,self.cellsize)
            pygame.draw.rect(self.surface,(255,0,0),dot)
                             

        for i in range(self.height):
            pygame.draw.line(self.surface,(0,0,0),(0,i*self.cellsize),(self.width*self.cellsize,i*self.cellsize))
        for i in range(self.width):
            pygame.draw.line(self.surface,(0,0,0),(i*self.cellsize,0),(i*self.cellsize,self.height*self.cellsize))


        pygame.display.update()