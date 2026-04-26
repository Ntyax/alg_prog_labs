import unittest
import os
import csv
from lab7 import solve_min_cable_length

class TestCableOptimization(unittest.TestCase):
    
    def setUp(self):
        self.filename = 'test_islands.csv'

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def create_csv(self, matrix):
        with open(self.filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(matrix)

    def test_basic_connection(self):
        matrix = [
            [0, 1, 5],
            [1, 0, 2],
            [5, 2, 0]
        ]
        self.create_csv(matrix)
        self.assertEqual(solve_min_cable_length(self.filename), 3.0)

    def test_single_island(self):
        matrix = [[0]]
        self.create_csv(matrix)
        self.assertEqual(solve_min_cable_length(self.filename), 0.0)

    def test_disconnected_graph(self):
        [0, float('inf')],
        [float('inf'), 0]
        self.create_csv(matrix)
        self.assertEqual(solve_min_cable_length(self.filename), -1)

if __name__ == '__main__':
    unittest.main()