import unittest
from unittest.mock import patch
import sys
sys.path.append("../src/")
from main import *
from Colors import *

class maintest(unittest.TestCase):

    def test_generateRandomPositionIsOk(self):
        xmax = 100
        ymax = 100
        x,y = generateRandomPosition(100,100).getX(),  generateRandomPosition(100,100).getY()
        self.assertTrue(0 <= x <= 100)
        self.assertTrue(0 <= y <= 100)
    
    def test_generateRandomPositionRaisedAnException(self):
        self.assertRaises(ValueError, lambda: generateRandomPosition(-5,-5))
    
    def test_generateRandomShipisOk(self):
        ship = generateRandomShip()
        self.assertIsInstance(ship, Ship, "generateRandomShip is instance of Ship")

    def test_generateRandomShipInSizePool(self):
        ship = generateRandomShip()
        self.assertIn(ship.getLifePoints(),[2,3,4,5])

    #Main method tests
    @patch("builtins.input") #Mocking user input
    def test_mainDoesNotAcceptsSizeSmallerThanTwo(self, mocked_input):
        mocked_input.side_effect = [1] #User inputs 1
        #Asserts that the main() method calls exit()
        self.assertRaises(SystemExit, lambda: main())
    
    @patch("builtins.input")
    def test_mainDoesNotAcceptsSizeGreaterThan26(self, mocked_input):
        mocked_input.side_effect = [42]
        self.assertRaises(SystemExit, lambda: main())

    @patch("builtins.input")
    def test_mainDoesNotAcceptsANegativeNumberOfShips(self, mocked_input):
        mocked_input.side_effect = [10, -3] #10 = board size, -3 = number of ships
        self.assertRaises(SystemExit, lambda: main())
        
if __name__ == '__main__':
    unittest.main()