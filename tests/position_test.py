import unittest
import sys
sys.path.append("../src/")
from Position import *

class position_test(unittest.TestCase):

    def test_PositionCreationIsOk(self):
        pos = Position(2,2)
        self.assertIsInstance(pos,Position, "Check if the position is well instance")

    def test_positionIsNotCreatedWhenYisNegative(self):
        self.assertRaises(ValueError, lambda: Position(2,-2))
    
    def test_positionIsNotCreatedWhenXIsNegative(self):
        self.assertRaises(ValueError, lambda: Position(-2,2))
    
    def test_positionGetX(self):
        pos = Position(2,3)
        self.assertEqual(pos.getX(),2)
    
    def test_positionGetY(self):
        pos = Position(3,2)
        self.assertEqual(pos.getY(),2)

    def test_positionToStringIsOk(self):
        pos = Position(2,2)
        self.assertEqual(pos.toString(),"C2")

    def test_createPositionWithLetterAndInt(self):
        pos = Position("A", 3)
        self.assertEqual("A3", pos.toString())

if __name__ == '__main__':
    unittest.main()
