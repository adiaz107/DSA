import unittest

from queue import Queue

class TestQueue(unittest.TestCase):

    def test_init(self):

        q = Queue()

        self.assertEqual(q.to_list(), [])

    def test_enqueue(self):

        q = Queue()

        q.enqueue("Alison")
        q.enqueue("Bob")
        q.enqueue("Chuck")
        q.enqueue("Diana")

        self.assertEqual(q.to_list(), ["Alison", "Bob", "Chuck", "Diana"])

    def test_dequeue(self):

        q = Queue()

        q.enqueue("Alison")
        q.enqueue("Bob")
        q.enqueue("Chuck")
        q.enqueue("Diana")

        q.dequeue()
        q.dequeue()

        self.assertEqual(q.to_list(), ["Chuck", "Diana"])

    def test_dequeue_empty(self):

        q = Queue()

        with self.assertRaises(Exception):
            q.dequeue()

    def test_top(self):

        q = Queue()

        q.enqueue("Alison")
        q.enqueue("Bob")
        q.enqueue("Chuck")
        q.enqueue("Diana")

        q.dequeue()
        q.dequeue()
        q.dequeue()

        self.assertEqual(q.top(), "Diana")

    def test_top_empty(self):

        q = Queue()

        with self.assertRaises(Exception):
            q.top()

if __name__ == '__main__':
    unittest.main()
