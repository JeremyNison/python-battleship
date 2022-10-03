from turtle import position
import unittest
from Board import *
from Ship import *
from Position import *
from Result import *
from Colors import *
import io, sys

class board_test(unittest.TestCase):

    #Test constructor
    #TODO
    
    #Testing that we can't set a ship vertically if the board is too small
    def test_setShipV1(self):
        board = Board(10,0) 
        ship = Ship(3)
        position = Position('A', 4)
        self.assertFalse(board.setShipV(ship,position))
        
    #Testing that we can't set a ship vertically at a position out of the board
    def test_setShipV2(self):
        board = Board(10,10) 
        ship = Ship(3)
        position = Position('D', 15)
        self.assertFalse(board.setShipV(ship,position))
        
        
    #Testing that we can't set a ship horizontally if the board is too small
    def test_setShipH1(self):
        board = Board(0,10) 
        ship = Ship(5)
        position = Position('B', 3)
        self.assertFalse(board.setShipH(ship,position))
        
    #Testing that we can't set a ship horizontally at a position out of board
    def test_setShipH2(self):
        board = Board(10,10) 
        ship = Ship(5)
        position = Position('B', 16)
        self.assertFalse(board.setShipH(ship,position))

    #ShootTest
    def test_shootAnEmptyCellReturnsMISSED(self):
        board = Board(10,10)
        result = board.shoot(3,4)
        self.assertEqual(Result.MISSED,result)
    
    def test_shootAShipReturnsHIT(self):
        board = Board(10,10)
        board.setShipH(Ship(3), Position('C', 3))
        self.assertEqual(Result.HIT, board.shoot(2,3))
        self.assertEqual(Result.HIT, board.shoot(3,3))

    def test_sunkingAShipReturnsSUNK(self):
        board=Board(1,1)
        board.setShipV(Ship(1), Position('A', 0))
        self.assertEqual(Result.SUNK, board.shoot(0,0))

    def test_shootOutsideTheBoardRaisesAnException(self):
        board = Board(2,2)
        self.assertRaises(Exception, lambda:board.shoot(2,2))
        self.assertRaises(Exception, lambda:board.shoot(0,2))
        self.assertRaises(Exception, lambda:board.shoot(2,0))
        try:
            board.shoot(0,1)
        except Exception:
            self.fail("shoot(0,1) shouldn't raise an exception")

    #Display Test
    #TODO : display non reveal, display shoot (MISSED | HIT/SUNK), display reveal 

    def test_display(self):
        s = " "+Colors.OKBLUE+"~"+Colors.ENDC
        board = Board(3,3)
        oracle = "  | A B C\n---------\n0 |"+s+s+s+"\n1 |"+s+s+s+"\n2 |"+s+s+s+"\n"
        captured_output = io.StringIO()
        sys.stdout = captured_output #redirect std output
        board.display()
        sys.stdout = sys.__stdout__ #Reset redirection

        self.assertEquals(oracle, captured_output.getvalue())

    def test_displayMissed(self):
        pass

    def test_displayHit(self):
        pass

    def test_displayReveal(self):
        pass

if __name__ == '__main__':
    unittest.main()