import unittest

from bst import BinarySearchTree

class TestBST(unittest.TestCase):

    def test_init(self):

        bst = BinarySearchTree()

        expected = None

        self.assertEqual(expected, bst.root)

    def test_add_single(self):

        bst = BinarySearchTree()

        bst.add(10)
        expected = 10

        self.assertEqual(expected, bst.root.data)

    def test_add_multiple(self):

        bst = BinarySearchTree()

        bst.add(10)
        bst.add(5)
        bst.add(20)
        bst.add(7)
        bst.add(21)
        bst.add(22)

        self.assertEqual(10, bst.root.data)
        self.assertEqual(5, bst.root.left.data)
        self.assertEqual(20, bst.root.right.data)
        self.assertEqual(7, bst.root.left.right.data)
        self.assertEqual(21, bst.root.right.right.data)

    def test_inorder(self):
        bst = BinarySearchTree()

        bst.add(13)
        bst.add(7)
        bst.add(29)
        bst.add(5)
        bst.add(11)
        bst.add(19)

        expected = [5, 7, 11, 13, 19, 29]

        self.assertEqual(expected, bst.inorder())

    def test_inorder_empty(self):
        bst = BinarySearchTree()

        expected = []

        self.assertEqual(expected, bst.inorder())

    def test_preorder(self):
        bst = BinarySearchTree()

        bst.add(13)
        bst.add(7)
        bst.add(29)
        bst.add(5)
        bst.add(11)
        bst.add(19)

        expected = [13, 7, 5, 11, 29, 19]

        self.assertEqual(expected, bst.preorder())

    def test_preorder_empty(self):
        bst = BinarySearchTree()

        expected = []

        self.assertEqual(expected, bst.preorder())

    def test_postorder(self):
        bst = BinarySearchTree()

        bst.add(13)
        bst.add(7)
        bst.add(29)
        bst.add(5)
        bst.add(11)
        bst.add(19)

        expected = [5, 11, 7, 19, 29, 13]

        self.assertEqual(expected, bst.postorder())

    def test_postorder_empty(self):
        bst = BinarySearchTree()

        expected = []

        self.assertEqual(expected, bst.postorder())

    def test_levelorder(self):
        bst = BinarySearchTree()

        bst.add(13)
        bst.add(7)
        bst.add(29)
        bst.add(5)
        bst.add(11)
        bst.add(19)

        expected = [13, 7, 29, 5, 11, 19]

        self.assertEqual(expected, bst.levelorder())

    def test_levelorder_empty(self):
        bst = BinarySearchTree()

        expected = []

        self.assertEqual(expected, bst.levelorder())

    def test_search(self):

        bst = BinarySearchTree()

        bst.add(100)
        bst.add(25)
        bst.add(1000)
        bst.add(43)
        bst.add(1)

        self.assertTrue(bst.search(100))
        self.assertFalse(bst.search(-1))

    def test_remove(self):
        bst = BinarySearchTree()

        bst.add(13)
        bst.add(7)
        bst.add(29)
        bst.add(5)
        bst.add(11)
        bst.add(19)
        bst.add(8)
        bst.add(12)
        bst.add(9)

        bst.remove(7)
        bst.remove(5)
        bst.remove(13)

        expected = [19, 8, 29, 11, 9, 12]

        self.assertEqual(expected, bst.levelorder())

if __name__ == '__main__':
    unittest.main()
