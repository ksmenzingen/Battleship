import pygame, Battlefield, Ship, Window
from Battlefield import *
from Ship import *
from Window import *


feld = BattleField(12,12)
feld.placeShip(Ship(4,'h',3,2))
feld.placeShip(Ship(6,'v',2,0))
feld.placeShip(Ship(4,'h',5,6))
feld.placeShip(Ship(3,'v',0,1))

cellsize = 20
pygame.init()
pygame.display.set_caption("Battleship")
window = Window(cellsize,12,12)

game_over = False
numShots = 0
shipsAlive = len(feld.ships)

delay = 100


while not game_over:
    print("Schiessen!")
    window.draw(feld)
    for event in pygame.event.get():
        # if event.type == pygame.QUIT:
        #     game_over = True
        #     break
        if event.type == pygame.MOUSEBUTTONDOWN:
            location = pygame.mouse.get_pos()
            x = int(location[0])//cellsize
            y = int(location[1])//cellsize
            if(feld.shoot(x,y)):
                print("TREFFER!")
                print()
                shipsAlive -= 1
            else:
                print("Daneben...")
                print()
            numShots += 1
            if(shipsAlive==0):
                game_over=True
            
    

print("Spielende! Du hast "+str(numShots)+" Schüsse benötigt.")
pygame.quit()