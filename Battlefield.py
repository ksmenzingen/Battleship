class BattleField:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.ships = []
        self.missedShots = []
        self.field = []


    def updateField(self):
        field = []
        for i in range(self.width):
            a = []
            for j in range(self.height):
                a.append(0)
            field.append(a)
        self.field = field

        for m in self.missedShots:
            field[m[0]][m[1]] = 'M'

        for s in self.ships:
            for i in range(len(s.coordinates)):
                if s.alive:
                    field[s.coordinates[i][0]][s.coordinates[i][1]] = 's'
                else:
                    field[s.coordinates[i][0]][s.coordinates[i][1]] = 'S'
        self.field = field


    def placeShip(self, ship):
        # out of Field ?
        if ship.coordinates[0][0] < 0 or ship.coordinates[0][1] < 0:
            return False
        elif ship.coordinates[-1][0] > self.width-1 or ship.coordinates[-1][1] > self.height-1:
            return False
        # crosses another ship ?
        for i in range(len(ship.coordinates)):
            for s in self.ships:
                if ship.coordinates[i] in s.coordinates:
                    return False
        # else: place ship  
        self.ships.append(ship)
        return True


    def shoot(self, x, y):
        # out of field ?
        if x<0 or y<0 or x>self.width-1 or y>self.height-1:
            return False

        # shot a ship?
        for i in range(len(self.ships)):
                if (x,y) in self.ships[i].coordinates:
                    self.ships[i].alive = False
                    self.updateField()
                    return True

        # else: missed shot
        self.missedShots.append((x,y))           
        return False


    def __str__(self):
        self.updateField()
        fieldString = "  "
        for i in range(self.width):
            if i//10 == 0:
                fieldString += " "
            fieldString += " "+str(i)+" "
        fieldString += "\n"+"  "+(4*self.width+1)*"-"+"\n"
        for i in range(self.height):
            fieldString += str(i)
            if i//10 == 0:
                fieldString += " "
            for j in range(self.width):
                if self.field[j][i] == 'S':
                    fieldString += "| S "
                elif self.field[j][i] == 'M':
                    fieldString += "| o "
                else:
                    fieldString += "|   "
            fieldString += "|\n"+"  "+(4*self.width+1)*"-"+"\n"
        return fieldString