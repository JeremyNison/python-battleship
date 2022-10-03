import unittest
from main import *

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

if __name__ == '__main__':
    unittest.main()