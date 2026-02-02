import unittest
from main import LinkedList

class TestLinkedList(unittest.TestCase):

    # Run before each test
    # def setUp(self):
    #     pass

    # Run once at the beginning
    # def setUpClass(self):
    #     pass

    def test_init(self):

        ll = LinkedList()
        self.assertEqual(ll.to_list(), [], 'LL should be empty at first!')

    def test_add_to_front(self):

        ll = LinkedList()
        ll.add_to_front(50)
        ll.add_to_front(60)
        ll.add_to_front(70)

        self.assertEqual(ll.to_list(), [70, 60, 50], 'LL does not match!')

    def test_add_to_back(self):

        ll = LinkedList()
        ll.add_to_back(70)
        ll.add_to_back(60)
        ll.add_to_back(50)

        self.assertEqual(ll.to_list(), [70, 60, 50], 'LL does not match!')

    def test_add_to_front_and_back(self):

        ll = LinkedList()
        ll.add_to_back(60)
        ll.add_to_back(50)
        ll.add_to_front(70)
        ll.add_to_front(80)
        ll.add_to_back(40)

        self.assertEqual(ll.to_list(), [80, 70, 60, 50, 40], 'LL does not match!')

    def test_add_to_index(self):

        ll = LinkedList()
        ll.add_to_index(70, 0)

        ll.add_to_index(40, 1)
        ll.add_to_index(60,1)
        ll.add_to_index(50, 2)
        ll.add_to_index(30, 4)

        self.assertEqual(ll.to_list(), [70, 60, 50, 40, 30], 'LL does not match!')

    def test_add_all(self):

        ll = LinkedList()

        ll.add_to_front(70) # 70
        ll.add_to_back(30) # 70, 30
        ll.add_to_index(50, 1) # 70, 50, 30
        ll.add_to_back(20) # 70, 50, 30, 20
        ll.add_to_index(40, 2) # 70, 50, 40, 30, 20
        ll.add_to_front(80) # 80, 70, 50, 40, 30, 20
        ll.add_to_index(60, 2) # 80, 70, 60, 50, 40, 30, 20

        self.assertEqual(ll.to_list(), [80, 70, 60, 50, 40, 30, 20], 'LL does not match!')

    def test_remove_from_front_1(self):

        ll = LinkedList()

        ll.add_to_front(80)
        ll.add_to_back(70)
        ll.add_to_back(60)
        ll.add_to_back(50)

        ll.remove_from_front()

        self.assertEqual(ll.to_list(), [70, 60, 50])

    def test_remove_from_front_2(self):

        ll = LinkedList()

        ll.add_to_front(80)
        ll.add_to_back(70)
        ll.add_to_back(60)
        ll.add_to_back(50)

        ll.remove_from_front()
        ll.remove_from_front()
        ll.remove_from_front()

        self.assertEqual(ll.to_list(), [50])

    def test_remove_from_front_empty(self):

        ll = LinkedList()

        with self.assertRaises(Exception):
            ll.remove_from_front()

    def test_remove_from_back(self):

        ll = LinkedList()

        ll.add_to_front(20)
        ll.add_to_front(30)
        ll.add_to_front(40)
        ll.add_to_front(50)
        ll.add_to_front(60)
        ll.add_to_front(70)

        ll.remove_from_back()
        ll.remove_from_back()
        ll.remove_from_back()

        self.assertEqual(ll.to_list(), [70, 60, 50])

    def test_remove_from_back_empty(self):

        ll = LinkedList()

        with self.assertRaises(Exception):
            ll.remove_from_back()

    def test_remove_from_index(self):

        ll = LinkedList()

        ll.add_to_front(50)
        ll.add_to_front(60)
        ll.add_to_front(70)
        ll.add_to_front(80)
        ll.add_to_front(90)

        ll.remove_from_index(3)
        ll.remove_from_index(3)

        self.assertEqual(ll.to_list(), [90, 80, 70])

    def test_get_index(self):

        ll = LinkedList()

        ll.add_to_front(50)
        ll.add_to_front(60)
        ll.add_to_front(70)
        ll.add_to_front(80)

        self.assertEqual(ll.get_index(2), 60)

    def test_get_index_negative_index(self):

        ll = LinkedList()

        ll.add_to_front(50)
        ll.add_to_front(60)
        ll.add_to_front(70)
        ll.add_to_front(80)

        with self.assertRaises(Exception):
            ll.get_index(-1)

    def test_get_index_out_of_bounds(self):

        ll = LinkedList()

        ll.add_to_front(50)
        ll.add_to_front(60)
        ll.add_to_front(70)
        ll.add_to_front(80)

        with self.assertRaises(Exception):
            ll.get_index(4)

    def test_search(self):

        ll = LinkedList()

        ll.add_to_front(90)
        ll.add_to_front(100)
        ll.add_to_front(110)
        ll.add_to_front(120)
        ll.add_to_front(130)
        ll.add_to_front(140)

        self.assertEqual(ll.search(110), 3)

    def test_search_data_not_in_ll(self):

        ll = LinkedList()

        ll.add_to_front(90)
        ll.add_to_front(100)
        ll.add_to_front(110)
        ll.add_to_front(120)
        ll.add_to_front(130)
        ll.add_to_front(140)

        self.assertEqual(ll.search(200), -1)


if __name__ == '__main__':
    unittest.main()
