from Cell import *
from Position import *
#This class represents a Board which contains Cells

class Board:

    #Creates a board with the given number of rows and columns and initialiezes empty cells
    def __init__(self, rows, columns):
        self.rows    = rows
        self.columns = columns

        #Contains all the cells of the board
        self.cells = []
        #Total life points of the board
        self.totalLifePoints = 0
        #Number of ships on the board
        self.numberOfShips = 0

        #Initializing empty cells
        for _ in range(rows):
            row = []
            for __ in range(columns):
                row.append(Cell())
            self.cells.append(row)

    #Sets the given ship vertically to the given position from top to bottom
    #Returns True if the ship has been palced, false otherwise (not enough room, error, ...)
    def setShipV(self, ship, position):
        x = position.getX()
        y = position.getY()
        cells = []

        try:
            #Check for room
            for i in range(y,y+ship.getLifePoints()):
                row = self.cells[i]
                cell = row[x]
                if not cell.isEmpty():
                    #Cannot place ship, space already occupied
                    return False
                cells.append(cell)
        except Exception:
            return False
        
        #Setting the ship into the cells
        self.__setShip__(cells, ship)
        return True

    #Sets the given ship horisontally to the given position fron right to left
    def setShipH(self, ship, position):
        x = position.getX()
        y = position.getY()
        cells = []

        try:
            row = self.cells[y]
            #Check for room
            for i in range(x, x+ship.getLifePoints()):
                cell = row[i]
                if not cell.isEmpty():
                    return False
                cells.append(cell)
        except Exception:
            return False

        #Setting the ship into the cells
        self.__setShip__(cells, ship)
        return True
    
    #Returns the total life points of the board
    def getTotalLifePoints(self):
        return self.totalLifePoints

    #Returns the number of ships alive on the board
    def getNumberOfShips(self):
        return self.numberOfShips

    #Shoots the cell at the given position and returns the result. 
    #Raises an exception if x or y is outside the board limits
    def shoot(self, x, y):
        if x < 0 or y < 0 or x >= self.rows or y >= self.columns:
            raise Exception("Shooting outside board boundaries is not allowed.")
        result = self.cells[y][x].shoot()

        if result == Result.HIT or result == Result.SUNK:
            self.totalLifePoints -= 1

        if result == Result.SUNK:
            self.numberOfShips -= 1

        return result
    
    #Displays the board
    def display(self, reveal = False):
        firstLine = "  |"
        secondLine = "---"
        for i in range(len(self.cells)):
            firstLine += " "+chr(ord('A') + i)
            secondLine += "--"

        print(firstLine)
        print(secondLine)

        for i in range(len(self.cells)):
            line = ""
            if(i < 10) :
                line = str(i)+" |"
            else:
                line = str(i)+"|"

            for cell in self.cells[i]:
                line += " "+cell.toString(reveal)
            print(line)

    #Places the given ship into each cell of the given list of cells and upgrades the board total lifepoints and number of ships
    def __setShip__(self, cells, ship):
        for cell in cells:
            cell.setShip(ship)    
        self.totalLifePoints += ship.getLifePoints()
        self.numberOfShips += 1

    def getRows(self):
        return self.rows

    def getColumns(self):
        return self.columns
