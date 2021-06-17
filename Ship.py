class Ship:
    def __init__(self, length, align, posX, posY):
        self.alive = True
        self.coordinates = []
        self.align = align
        
        if align == 'h':
            for i in range (length):
                self.coordinates.append((posX+i,posY))
        elif align == 'v':
            for i in range (length):
                self.coordinates.append((posX,posY+i))