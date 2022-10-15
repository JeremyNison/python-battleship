import unittest
import sys
sys.path.append("../src/")
from Cell import *
from Ship import *
from Result import *

class cell_test(unittest.TestCase):

    def setUp(self):
        self.cell = Cell()

    #Test constructor
    def test_init(self):
        self.assertFalse(self.cell.shot)
        self.assertIsNone(self.cell.ship)

    def test_setShip(self):
        ship = Ship(4)
        self.cell.setShip(ship)
        self.assertEqual(ship,self.cell.ship)

    def test_isEmpty(self):
        ship = Ship(3)
        self.assertTrue(self.cell.isEmpty())
        self.cell.setShip(ship)
        self.assertFalse(self.cell.isEmpty())

    #Shoot test
    def test_shoot_sets_cell_shot_to_true(self):
        self.assertFalse(self.cell.shot)
        self.cell.shoot()
        self.assertTrue(self.cell.shot)

    def test_shoot_return_missed_if_cell_is_empty(self):
        self.assertEqual(Result.MISSED,self.cell.shoot())

    def test_shoot_return_hit_if_cell_contains_a_ship(self):
        self.cell.setShip(Ship(3))
        self.assertEqual(Result.HIT,self.cell.shoot())

    def test_shoot_return_sunk_if_ship_is_sunk(self):
        self.cell.setShip(Ship(1))
        self.assertEqual(Result.SUNK,self.cell.shoot())

    def test_shoot_return_missed_if_cell_alrady_shoot(self):
        self.cell.setShip(Ship(2))
        self.cell.shoot()
        self.assertEqual(Result.MISSED,self.cell.shoot())

    #ToString test
    def test_to_string_untoutched(self):
        self.assertEqual(Colors.OKBLUE+"~"+Colors.ENDC,self.cell.toString())

    def test_to_string_missed(self):
        self.cell.shoot()
        self.assertEqual(Colors.WARNING+"x"+Colors.ENDC,self.cell.toString())
    
    def test_to_string_hit(self):
        self.cell.setShip(Ship(1))
        self.cell.shoot()
        self.assertEqual(Colors.FAIL+"H"+Colors.ENDC,self.cell.toString())

    def test_to_string_empty_reveal(self):
        self.assertEqual(Colors.OKBLUE+"~"+Colors.ENDC,self.cell.toString(True))

    def test_to_string_boat_reveal(self):
        self.cell.setShip(Ship(1))
        self.assertEqual(Colors.OKGREEN+"B"+Colors.ENDC,self.cell.toString(True))

if __name__ == '__main__':
    unittest.main()