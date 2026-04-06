import unittest
from lab5 import flood_fill  

class TestFloodFill(unittest.TestCase):

    def test_basic_fill(self):
        matrix = [
            ['W', 'W', 'B'],
            ['W', 'B', 'B'],
            ['B', 'B', 'B']
        ]
        flood_fill(matrix, 0, 0, 'W', 'G')
        
        expected = [
            ['G', 'G', 'B'],
            ['G', 'B', 'B'],
            ['B', 'B', 'B']
        ]
        self.assertEqual(matrix, expected)

    def test_no_fill_needed(self):
        matrix = [['R', 'R'], ['R', 'R']]
        flood_fill(matrix, 0, 0, 'R', 'R')
        
        expected = [['R', 'R'], ['R', 'R']]
        self.assertEqual(matrix, expected)

    def test_isolated_area(self):
        matrix = [
            ['R', 'B', 'R'],
            ['B', 'B', 'B'],
            ['R', 'B', 'R']
        ]
        flood_fill(matrix, 1, 1, 'B', 'W')

        expected = [
            ['R', 'W', 'R'],
            ['W', 'W', 'W'],
            ['R', 'W', 'R']
        ]
        self.assertEqual(matrix, expected)

    def test_out_of_bounds(self):
        matrix = [['R']]
        try:
            flood_fill(matrix, 5, 5, 'R', 'G')
            flood_fill(matrix, -1, 0, 'R', 'G')
        except IndexError:
            self.fail("flood_fill raised IndexError unexpectedly!")

if __name__ == '__main__':
    unittest.main()