import unittest
from lab3 import BinaryTree

class TestFindSuccessor(unittest.TestCase):
    def test_successor_of_7_is_10(self):
        root = BinaryTree(10)

        node5 = BinaryTree(5, parent=root)
        node3 = BinaryTree(3, parent=node5)
        node7 = BinaryTree(7, parent=node5)
        root.left = node5
        node5.left = node3
        node5.right = node7

        node15 = BinaryTree(15, parent=root)
        node20 = BinaryTree(20, parent=node15)
        node12 = BinaryTree(12, parent=node20)
        root.right = node15
        node15.right = node20
        node20.left = node12

        result = root.find_successor(node7)
        
        self.assertIsNotNone(result)
        self.assertEqual(result.value, 10)

if __name__ == "__main__":
    unittest.main(verbosity=2)