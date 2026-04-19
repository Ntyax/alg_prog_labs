import unittest
from lab6 import solve_server_placement

class TestGameServer(unittest.TestCase):
    
    def test_example_1(self):
        n = 6
        clients = {1, 2, 6}
        edges = [
            (1, 2, 6), (1, 3, 10), (3, 4, 80), 
            (4, 5, 50), (5, 6, 20), (2, 3, 40), (2, 4, 100)
        ]
        self.assertEqual(solve_server_placement(n, clients, edges), 100)

    def test_example_2(self):
        n = 9
        clients = {2, 4, 6}
        edges = [
            (1, 2, 20), (2, 3, 20), (3, 6, 20), (6, 9, 20),
            (9, 8, 20), (8, 7, 20), (7, 4, 20), (4, 1, 20),
            (5, 2, 10), (5, 4, 10), (5, 6, 10), (5, 8, 10)
        ]
        self.assertEqual(solve_server_placement(n, clients, edges), 10)

    def test_example_3(self):
        n = 3
        clients = {1, 3}
        edges = [
            (1, 2, 50), (2, 3, 1000000000)
        ]
        self.assertEqual(solve_server_placement(n, clients, edges), 1000000000)

if __name__ == '__main__':
    unittest.main()