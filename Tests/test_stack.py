import unittest

from stack import Stack

class TestStack(unittest.TestCase):

    def test_push(self):

        stack = Stack()

        stack.push(50)
        stack.push(60)
        stack.push(70)

        self.assertEqual(stack.to_list(), [70, 60, 50])

    def test_pop(self):

        stack = Stack()

        stack.push(50)
        stack.push(60)
        stack.push(70)
        stack.push(80)

        stack.pop()

        self.assertEqual(stack.pop(), 70)

    def test_pop_empty(self):

        stack = Stack()

        with self.assertRaises(Exception):
            stack.pop()

    def test_peek(self):

        stack = Stack()

        stack.push(50)
        stack.push(60)
        stack.push(70)

        self.assertEqual(stack.peek(), 70)

    def test_peek_empty(self):

        stack = Stack()

        with self.assertRaises(Exception):
            stack.peek()

    def test_clear(self):

        stack = Stack()

        stack.push(100)
        stack.push(150)
        stack.push(200)
        stack.push(100)
        stack.push(150)
        stack.push(200)

        stack.pop()
        stack.pop()

        stack.clear()

        self.assertEqual(stack.size, 0)

if __name__ == '__main__':
    unittest.main()
