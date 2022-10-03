#This class is used to describe a position.
#A position can be described by a letter and a number (ex : B4) or with coordinates (2,4)

class Position:

    def __init__(self, x, y):
        if y < 0:
            raise ValueError("y must be positive")
        if x < 0:
            raise ValueError("x must be positive")
        
        if type(x) is str:
            #Converting the letter to a coordinate position
            self.x = ord(x) - ord('A')
        else:
            self.x = x
        self.y = int(y)
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y

    def toString(self):
        #Converting int to letter
        if type(self.x) is int:
            return chr(ord('A') + self.x)+str(self.y)