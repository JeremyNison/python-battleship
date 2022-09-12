from Result import *
from Colors import *
#This class represents a cell which can contains a Ship

class Cell:

    def __init__(self):
        self.shot = False
        self.ship = None

    #Sets the given ship in the cell
    def setShip(self, ship):
        self.ship = ship

    #Returns true if the cell does not contains any ship, false otherwise
    def isEmpty(self):
        return self.ship is None
    
    #Shoots the cell. Returns the appropriate Result(MISSED, HIT or SUNK)
    def shoot(self):
        if self.shot: #If the cell has already benn shot, return Missed to avoid hitting the same cell
            return Result.MISSED

        self.shot = True
        if self.isEmpty():
            return Result.MISSED
        else:
            if self.ship.shoot() == 0:
                return Result.SUNK
            else:
                return Result.HIT
    
    #Returns the appropriate caracter regarding to the cell's current state (untoutched, shoot)
    def toString(self, reveal = False):
        if not self.isEmpty() and reveal:
            return Colors.OKGREEN+"B"+Colors.ENDC #Reveals the position of the boat
        elif not self.shot: #untoutched cell
            return Colors.OKBLUE+"~"+Colors.ENDC
        elif self.shot and self.isEmpty(): #missed (empty cell)
            return Colors.WARNING+"x"+Colors.ENDC  
        else: #hit
            return Colors.FAIL+"H"+Colors.ENDC  