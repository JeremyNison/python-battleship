import unittest
import sys
sys.path.append("../src/")
from Ship import *

class ShipTest(unittest.TestCase):
    
    def test_getLifePoints(self):
        ship = Ship(2)
        self.assertEqual(ship.getLifePoints(), 2)

    def test_shoot(self):
        ship = Ship(2)
        self.assertEqual(ship.shoot(), 1)

    def test_isSunk(self):
        ship = Ship(1)
        self.assertFalse(ship.isSunk())
        ship.shoot()
        self.assertTrue(ship.isSunk())
        
if __name__ == '__main__':
    unittest.main()