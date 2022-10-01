import unittest
from Board import *
from Ship import *
from Position import *

class board_test(unittest.TestCase):
    
    #Testing that we can't set a ship vertically if the board is too small
    def test_setShipV(self):
        board = Board(10,0) 
        ship = Ship(5)
        position = Position('A', 4)
        self.assertFalse(board.setShipV(ship,position))
        
    #Testing that we can't set a ship horizontally if the board is too small
    def test_setShipH(self):
        board = Board(0,10) 
        ship = Ship(5)
        position = Position('B', 3)
        self.assertFalse(board.setShipH(ship,position))
        
        
if __name__ == '__main__':
    unittest.main()