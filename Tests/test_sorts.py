import unittest

from sorts import bubble_sort, insertion_sort, selection_sort

class TestSorts(unittest.TestCase):

    def test_bubble_sort(self):

        arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]

        arr_sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        comparisons = 36
        expected = arr_sorted, comparisons

        self.assertEqual(expected, bubble_sort(arr))

    def test_bubble_sort_sorted(self):

        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        arr_sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        comparisons = 8
        expected = arr_sorted, comparisons

        self.assertEqual(expected, bubble_sort(arr))

    def test_bubble_sort_random(self):

        arr = [5, 8, 7, 13, 3, 1, 8, 8, 10, 1, 11, 4]

        arr_sorted = [1, 1, 3, 4, 5, 7, 8, 8, 8, 10, 11, 13]
        comparisons = 63
        expected = arr_sorted, comparisons

        self.assertEqual(expected, bubble_sort(arr))

    def test_insertion_sort(self):

        arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

        arr_sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        comparisons = 45
        expected = arr_sorted, comparisons

        actual = insertion_sort(arr)

        self.assertEqual(expected, actual)

    def test_insertion_sort_sorted(self):

        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        arr_sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        comparisons = 9
        expected = arr_sorted, comparisons

        actual = insertion_sort(arr)

        self.assertEqual(expected, actual)

    def test_selection_sort(self):

        arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]

        arr_sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        comparisons = 36
        expected = arr_sorted, comparisons

        self.assertEqual(expected, selection_sort(arr))

if __name__ == '__main__':
    unittest.main()
