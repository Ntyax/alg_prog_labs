import unittest
from lab4 import RedBlackPriorityQueue

class TestRedBlackPriorityQueue(unittest.TestCase):

    def setUp(self):
        self.pq = RedBlackPriorityQueue()

    def test_insert_and_peek(self):
        self.pq.insert("Task Low", 100)
        self.pq.insert("Task High", 10)
        self.pq.insert("Task Medium", 50)

        value, priority = self.pq.peek()
        self.assertEqual(value, "Task High")
        self.assertEqual(priority, 10)

    def test_extract_max_order(self):
        items = [("C", 30), ("A", 10), ("B", 20), ("D", 40)]
        for val, prio in items:
            self.pq.insert(val, prio)

        self.assertEqual(self.pq.extract_max(), ("A", 10))
        self.assertEqual(self.pq.extract_max(), ("B", 20))
        self.assertEqual(self.pq.extract_max(), ("C", 30))
        self.assertEqual(self.pq.extract_max(), ("D", 40))

    def test_empty_queue_raises_error(self):
        with self.assertRaises(IndexError):
            self.pq.peek()
        with self.assertRaises(IndexError):
            self.pq.extract_max()

    def test_peek_all_sorted(self):
        data = [("Low", 50), ("High", 10), ("Mid", 30)]
        for v, p in data:
            self.pq.insert(v, p)
            
        all_elements = self.pq.peek_all()
        priorities = [p for v, p in all_elements]
        self.assertEqual(priorities, [10, 30, 50])

    def test_multiple_same_priorities(self):
        self.pq.insert("Task 1", 10)
        self.pq.insert("Task 2", 10)
        
        res1 = self.pq.extract_max()
        res2 = self.pq.extract_max()
        
        self.assertEqual(res1[1], 10)
        self.assertEqual(res2[1], 10)

if __name__ == '__main__':
    unittest.main()