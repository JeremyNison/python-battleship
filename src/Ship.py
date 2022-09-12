#This class represents a Ship

class Ship:

    #Creates a new ship with the given length
    def __init__(self, length):
        self.lifePoints = length

    #Returns the remaining life points of the ship
    def getLifePoints(self):
        return self.lifePoints

    #Decreases the ship lifepoints by 1 and return the life points of the ship
    def shoot(self):
        self.lifePoints -= 1
        return self.lifePoints

    #Returns True if the ship has 0 life points, False otherwise
    def isSunk(self):
        if self.lifePoints <= 0:
            return True
        return False 