import unittest
from Board import *
from Ship import *
from Position import *
from Result import *
from Colors import *
import io, sys

#Useful macros
s = " "+Colors.OKBLUE+"~"+Colors.ENDC
m = " "+Colors.WARNING+"x"+Colors.ENDC
h = " "+Colors.FAIL+"H"+Colors.ENDC
b = " "+Colors.OKGREEN+"B"+Colors.ENDC

class board_test(unittest.TestCase):

    #Test constructor
    def test_init(self):
        rows = 10
        columns = 10 
        board = Board(rows,columns)
        self.assertTrue(board.rows == rows)
        self.assertTrue(board.columns == columns)
        self.assertFalse(board.cells == [])
        self.assertTrue(board.totalLifePoints == 0)
        self.assertTrue(board.numberOfShips == 0)
    
    #Testing that we can't create a board with negative rows and columns
    def test_negativ_init(self):
        negativ_rows = -10
        negativ_columns = -10
        negativ_board = Board(negativ_rows,negativ_columns)
        self.assertTrue(negativ_board.rows == negativ_rows)
        self.assertTrue(negativ_board.columns == negativ_columns)
        self.assertTrue(negativ_board.cells == [])
        self.assertTrue(negativ_board.totalLifePoints == 0)
        self.assertTrue(negativ_board.numberOfShips == 0)
        
    
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
        
    #Testing that we can't set a ship horizontally at a position out of the board
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
    def test_display(self):
        board = Board(3,3)
        oracle = "  | A B C\n---------\n0 |"+s+s+s+"\n1 |"+s+s+s+"\n2 |"+s+s+s+"\n"

        captured_output = io.StringIO()
        sys.stdout = captured_output #redirect std output
        board.display()
        sys.stdout = sys.__stdout__ #Reset redirection

        self.assertEquals(oracle, captured_output.getvalue())

    def test_displayMissed(self):
        board = Board(3,3)
        oracle = "  | A B C\n---------\n0 |"+m+s+s+"\n1 |"+s+s+s+"\n2 |"+s+s+m+"\n"

        captured_output = io.StringIO()
        sys.stdout = captured_output

        board.shoot(0,0)
        board.shoot(2,2)

        board.display()
        sys.stdout = sys.__stdout__

        self.assertEqual(oracle, captured_output.getvalue())

    def test_displayHit(self):
        board = Board(3,3)
        oracle = "  | A B C\n---------\n0 |"+s+h+s+"\n1 |"+s+s+s+"\n2 |"+s+s+s+"\n"

        captured_output = io.StringIO()
        sys.stdout = captured_output

        board.setShipH(Ship(2),Position('B',0))
        board.shoot(1,0)

        board.display() 
        self.assertEqual(oracle, captured_output.getvalue())

        captured_output = io.StringIO()
        sys.stdout = captured_output

        oracle = "  | A B C\n---------\n0 |"+s+h+h+"\n1 |"+s+s+s+"\n2 |"+s+s+s+"\n"
        board.shoot(2,0)

        board.display()
        sys.stdout = sys.__stdout__

        self.assertEqual(oracle, captured_output.getvalue())

    def test_displayReveal(self):
        board = Board(3,3)
        oracle = "  | A B C\n---------\n0 |"+s+s+s+"\n1 |"+b+b+b+"\n2 |"+s+s+s+"\n"

        board.setShipH(Ship(3),Position('A',1))

        captured_output = io.StringIO()
        sys.stdout = captured_output

        board.display(True)
        sys.stdout = sys.__stdout__

        self.assertEqual(oracle, captured_output.getvalue())

if __name__ == '__main__':
    unittest.main()