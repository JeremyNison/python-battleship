import unittest
from Ship import *

class ShipTest(unittest.TestCase):

    def test_getLifePoints(self):
        ship = Ship(4)
        self.assertEqual(ship.getLifePoints(), 4)

if __name__ == '__main__':
    unittest.main()