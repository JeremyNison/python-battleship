import unittest
from unittest.mock import patch
import sys
from random import randrange, sample
sys.path.append("../src/")
from main import *
from Colors import *

class main_test(unittest.TestCase):

    def test_generateRandomPosition(self):
        #Generating a position with two random boundaries 100000 times
        for _ in range(100000):
            xmax = randrange(1,10000)
            ymax = randrange(1,10000)
            position = generateRandomPosition(xmax, ymax)
            self.assertTrue(0 <= position.getX() <= xmax)
            self.assertTrue(0 <= position.getY() <= ymax)
    
    def test_generateRandomPositionRaisedAnException(self):
        self.assertRaises(ValueError, lambda: generateRandomPosition(1,-3))
        self.assertRaises(ValueError, lambda: generateRandomPosition(-2,6))
        self.assertRaises(ValueError, lambda: generateRandomPosition(-5,-12))
        self.assertRaises(ValueError, lambda: generateRandomPosition(0,0))
    
    def test_generateRandomShipisOk(self):
        ship = generateRandomShip()
        self.assertIsInstance(ship, Ship, "generateRandomShip is instance of Ship")

    def test_generateRandomShipInSizePool(self):
        for _ in range(10000):
            size_pool = sample(range(1, 100), randrange(1,50))
            ship = generateRandomShip(size_pool)
            self.assertIn(ship.getLifePoints(),size_pool)

    #randomPopulate tests
    def test_randomPopulateGeneratesTheRightNumberOfShips(self):
        for _ in range(10000):
            board = Board(10,10)
            nship = randrange(1,10)
            randomPopulate(board, nship)
            self.assertEqual(nship, board.numberOfShips)

    def test_randomPopulateStopsIfAShipCannotBePlaced(self):
        for _ in range(1000):
            board = Board(2,2)
            board.setShipV(Ship(2), Position("A",0))
            board.setShipV(Ship(2), Position("B",0))
            self.assertRaises (SystemExit, lambda: randomPopulate(board, 1, 1))

    #Main method tests
    @patch("builtins.input") #Mocking user input
    def test_mainDoesNotAcceptsSizeSmallerThanTwo(self, mocked_input):
        mocked_input.side_effect = [1] #User inputs 1
        #Asserts that the main() method calls exit()
        self.assertRaises(SystemExit, lambda: main())

    @patch("builtins.input")
    def test_mainDoesNotAcceptsIncorrectBoardSize(self, mocked_input):
        mocked_input.side_effect = ["definitly_not_a_valid_board_size"]
        self.assertRaises(SystemExit, lambda: main())
    
    @patch("builtins.input")
    def test_mainDoesNotAcceptsSizeGreaterThan26(self, mocked_input):
        mocked_input.side_effect = [42]
        self.assertRaises(SystemExit, lambda: main())

    @patch("builtins.input")
    def test_mainDoesNotAcceptsANegativeNumberOfShips(self, mocked_input):
        mocked_input.side_effect = [10, -3] #10 = board size, -3 = number of ships
        self.assertRaises(SystemExit, lambda: main())

    @patch("builtins.input")
    def test_mainDoesNotAcceptsIncorrectShipNumber(self, mocked_input):
        mocked_input.side_effect = [2, "somerandomstring"]
        self.assertRaises(SystemExit, lambda: main())

    @patch("builtins.input")
    def test_gameEndWhenUserTypesReveal(self, mocked_input):
        mocked_input.side_effect = [3, 1, "reveal"]
        self.assertRaises(SystemExit, lambda: main())

    @patch("builtins.input")
    def test_gameEndWhenAllShipsAreSunk(self, mocked_input):
        #Creating a board of size 3 with one ship, and shooting all the cells
        mocked_input.side_effect = [3, 1, "A0", "B0", "C0", "A1", "B1", "C1", "A2", "B2", "C2"]
        self.assertRaises(SystemExit, lambda: main())

if __name__ == '__main__':
    unittest.main()