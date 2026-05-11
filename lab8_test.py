import unittest
import os
from lab8 import solve_ijones

class TestIJones(unittest.TestCase):
    
    def setup_file(self, content):
        with open('ijones.in', 'w') as f:
            f.write(content)

    def read_output(self):
        if os.path.exists('ijones.out'):
            with open('ijones.out', 'r') as f:
                return int(f.read().strip())
        return None

    def test_example_1(self):
        self.setup_file("3 3\naaa\ncab\ndef")
        solve_ijones()
        self.assertEqual(self.read_output(), 5)

    def test_example_2(self):
        self.setup_file("10 1\nabcdefaghi")
        solve_ijones()
        self.assertEqual(self.read_output(), 5)

    def test_example_3(self):
        self.setup_file("7 6\naaaaaaa\naaaaaaa\naaaaaaa\naaaaaaa\naaaaaaa\naaaaaaa")
        solve_ijones()
        self.assertEqual(self.read_output(), 5)

if __name__ == '__main__':
    unittest.main()