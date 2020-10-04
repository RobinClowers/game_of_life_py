import unittest
from unittest.mock import patch
from game import *


class TestGame(unittest.TestCase):
    @patch('builtins.print')
    @patch('os.system')
    def test_next_generation(self, mockedPrint, mockedSystem):
        self.assertEqual(next_generation([
            [0, 0, 1],
            [0, 1, 1],
            [0, 0, 1],
        ]), [
            [0, 1, 1],
            [0, 1, 1],
            [0, 1, 1],
        ])

    def test_neighbours(self):
        board = [
            [0, 0, 1],
            [0, 1, 1],
            [0, 0, 1],
        ]
        self.assertEqual(neighbours(board, 0, 0), 1)
        self.assertEqual(neighbours(board, 1, 0), 3)
        self.assertEqual(neighbours(board, 2, 0), 2)
        self.assertEqual(neighbours(board, 0, 1), 1)
        self.assertEqual(neighbours(board, 1, 1), 3)
        self.assertEqual(neighbours(board, 2, 1), 3)
        self.assertEqual(neighbours(board, 0, 2), 1)
        self.assertEqual(neighbours(board, 1, 2), 3)
        self.assertEqual(neighbours(board, 2, 2), 2)

    def test_live_cell_with_one_neighbour_dies(self):
        self.assertFalse(cell_lives(True, 1))

    def test_live_cell_with_two_neighbours_lives(self):
        self.assertTrue(cell_lives(True, 2))

    def test_live_cell_with_three_neighbours_lives(self):
        self.assertTrue(cell_lives(True, 3))

    def test_live_cell_with_four_neighbours_dies(self):
        self.assertFalse(cell_lives(True, 4))

    def test_dead_cell_with_two_neighbours_stays_dead(self):
        self.assertFalse(cell_lives(False, 2))

    def test_dead_cell_with_three_neighbours_comes_alive(self):
        self.assertTrue(cell_lives(False, 3))

    def test_dead_cell_with_four_neighbours_stays_dead(self):
        self.assertFalse(cell_lives(False, 4))


if __name__ == '__main__':
    unittest.main()
