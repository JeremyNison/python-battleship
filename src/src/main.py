from Board import *
from Position import *
from Ship import *
from Result import *
from Colors import *
import random

#Populates randomly the given board.
#Generates random ships and place them randomly onto the board
def randomPopulate(board, nships, maxTry = 10000):
    for _ in range(nships):
        ship = generateRandomShip()
        size = board.getRows()
        position = generateRandomPosition(size, size)
        nbTry = 0 #Numbers of attemps to place a ship

        #Vertical or horisontal
        dir = random.randrange(2)
        if dir == 0: #Vertical
            while not board.setShipV(ship, position):
                if nbTry > maxTry:
                    print(Colors.FAIL+"Too many ships on the board. Consider reduicing the amount of ships to place."+Colors.ENDC)
                    exit()
                position = generateRandomPosition(size, size)
                nbTry +=1
        else: #Horisontal
            while not board.setShipH(ship, position):
                if nbTry > maxTry:
                    print(Colors.FAIL+"Too many ships on the board. Consider reduicing the amount of ships to place."+Colors.ENDC)
                    exit()
                position = generateRandomPosition(size, size)
                nbTry +=1
    
#Generates a random position within the board
def generateRandomPosition(xmax, ymax):
    x = random.randrange(0,xmax)
    y = random.randrange(0,ymax)

    return Position(x,y)
    
#Generates a random ship
def generateRandomShip():
    sizePool = [2,2,3,3,3,3,4,4,5] #Pool of different ship sizes
    sizeIndex = random.randrange(0,len(sizePool))
    random.shuffle(sizePool)

    #Picking a random size and generating a ship
    return Ship(sizePool[sizeIndex])

def main():
    #Initialization
    print(Colors.HEADER+"Enter board size (max 26) "+Colors.ENDC)
    size = int(input(">>> "))

    if size < 2:
        print(Colors.FAIL+"Board too small"+Colors.ENDC)
        exit()
    
    #Checking max size
    if size > 26:
        print(Colors.FAIL+"Grid too fat."+Colors.ENDC)
        exit()

    print(Colors.HEADER+"Enter number of ships"+Colors.ENDC)
    try:
        nships = int(input(">>> "))
    except:
        print(Colors.FAIL+"Please enter a number."+Colors.ENDC)
        exit()

    if nships < 1:
        print(Colors.FAIL+"Number of ship must be positive"+Colors.ENDC)
        exit()

    #Creating the board
    board = Board(size,size)

    #Creating and placing the ships
    randomPopulate(board, nships)

    board.display()

    separator = '---'+'--' * size

    #Playing
    while board.getTotalLifePoints() > 0:
        print(separator)
        print(Colors.HEADER+"Enter a position to strike"+Colors.ENDC)
        position = input(">>> ")

        #To reveal the board and end the game
        if position.lower() == "reveal":
            board.display(True)
            print(Colors.FAIL+"Game over."+Colors.ENDC)
            exit()

        #Creating position object
        x = position[0]
        y = position[1:]

        try:
            position = Position(x, y)
        except:
            print(Colors.FAIL+"Invalid input. Retry."+Colors.ENDC)
            continue

        #Shooting
        try:
            result = board.shoot(position.getX(), position.getY())
        except Exception:
            print(Colors.FAIL+"Failed to shoot this position. Please retry."+Colors.ENDC)
            continue

        print(Colors.OKCYAN+"You shooted position "+position.toString()+Colors.ENDC)
        if result == Result.MISSED:
            print(Colors.WARNING+"MISSED !"+Colors.ENDC)
        elif result == Result.HIT:
            print(Colors.OKGREEN+"HIT !"+Colors.ENDC)
        else:
            print(Colors.OKGREEN+"SUNK ! Remaining boats : "+str(board.getNumberOfShips())+Colors.ENDC)

        board.display()

    #No lifepoints : end of the game
    print(Colors.OKGREEN+"Well played, you win !"+Colors.ENDC)

if __name__ == '__main__':
    main()