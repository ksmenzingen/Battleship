from Battlefield import *
from Ship import *


feld = BattleField(12,12)
feld.placeShip(Ship(4,'h',3,2))
feld.placeShip(Ship(6,'v',2,0))
feld.placeShip(Ship(4,'h',5,6))
feld.placeShip(Ship(3,'v',0,1))

game_over = False
numShots = 0
shipsAlive = len(feld.ships)

while not game_over:
    print(feld)
    print("Schiessen!")
    x=int(input("x-Koordinate: "))
    y=int(input("y-Koordinate: "))
    if(feld.shoot(x,y)):
        print("TREFFER!")
        print()
        shipsAlive -= 1
    else:
        print("Daneben...")
        print()
    numShots += 1
    if(shipsAlive==0):
        game_over = True

print("Spielende! Du hast "+str(numShots)+" Schüsse benötigt.")