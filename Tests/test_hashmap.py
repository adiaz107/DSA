import unittest

from hash_map import HashMap

class TestHashMap(unittest.TestCase):

    def test_hash(self):

        hmap = HashMap()

        self.assertEqual(hmap.hash('July 20'), 0)
        self.assertEqual(hmap.hash('April 27'), 1)
        self.assertEqual(hmap.hash('March 30'), 2)
        self.assertEqual(hmap.hash('April 29'), 3)
        self.assertEqual(hmap.hash('February 2'), 4)
        self.assertEqual(hmap.hash('October 18'), 5)
        self.assertEqual(hmap.hash('September 1'), 6)
        self.assertEqual(hmap.hash('March 6'), 7)
        self.assertEqual(hmap.hash('March 17'), 7)
        self.assertEqual(hmap.hash('May 13'), 7)
        self.assertEqual(hmap.hash('November 19'), 8)
        self.assertEqual(hmap.hash('December 8'), 9)

    def test_put(self):

        hmap = HashMap()

        hmap.put('July 20', 900)
        hmap.put('March 30', 800)
        hmap.put('March 6', 700)
        hmap.put('March 17', 600)
        hmap.put('December 8', 500)

        expected = [[('July 20', 900)], [], [('March 30', 800)], [], [],
                    [], [], [('March 6', 700), ('March 17', 600)], [], [('December 8', 500)], ]

        self.assertEqual(hmap.table, expected)

    def test_get(self):

        hmap = HashMap()

        hmap.put('July 20', 900)
        hmap.put('March 30', 800)
        hmap.put('March 6', 700)
        hmap.put('March 17', 600)
        hmap.put('December 8', 500)

        self.assertEqual(hmap.get('July 20'), 900)
        self.assertEqual(hmap.get('March 17'), 600)
        self.assertEqual(hmap.get('December 8'), 500)

    def test_get_key_not_found(self):
        hmap = HashMap()

        hmap.put('July 20', 900)
        hmap.put('March 30', 800)
        hmap.put('March 6', 700)
        hmap.put('March 17', 600)
        hmap.put('December 8', 500)

        with self.assertRaises(Exception):
            hmap.get('May 13')

    def test_get_key_not_found_2(self):
        hmap = HashMap()

        hmap.put('July 20', 900)
        hmap.put('March 30', 800)
        hmap.put('March 6', 700)
        hmap.put('March 17', 600)
        hmap.put('December 8', 500)

        with self.assertRaises(Exception):
            hmap.get('January 1')

    def test_delete(self):

        hmap = HashMap()

        hmap.put('July 20', 900)
        hmap.put('March 30', 800)
        hmap.put('March 6', 700)
        hmap.put('March 17', 600)
        hmap.put('December 8', 500)

        hmap.delete('March 6')
        hmap.delete('December 8')

        expected = [[('July 20', 900)], [], [('March 30', 800)], [], [],
                    [], [], [('March 17', 600)], [], [], ]

        self.assertEqual(hmap.table, expected)

    def test_delete_key_not_found(self):

        hmap = HashMap()

        hmap.put('July 20', 900)
        hmap.put('March 30', 800)
        hmap.put('March 6', 700)
        hmap.put('March 17', 600)
        hmap.put('December 8', 500)

        with self.assertRaises(Exception):
            hmap.delete('May 13')

    def test_resize(self):

        hmap = HashMap()

        hmap.put('July 20', 900)
        hmap.put('March 30', 800)
        hmap.put('March 6', 700)
        hmap.put('March 17', 600)
        hmap.put('May 13', 500)
        hmap.put('November 19', 400)

        expected = [[('July 20', 900)], [], [('March 30', 800)],
                    [], [], [],
                    [], [('March 6', 700), ('March 17', 600), ('May 13', 500)],
                    [('November 19', 400)], [], ]

        self.assertEqual(hmap.table, expected)

        hmap.put('December 8', 300)

        expected = [[], [], [('November 19', 400)],
                    [], [('July 20', 900)], [],
                    [], [('May 13', 500)], [],
                    [], [('March 6', 700)], [],
                    [], [('March 30', 800)], [],
                    [], [], [],
                    [('March 17', 600), ('December 8', 300)], [], [], ]

        self.assertEqual(hmap.table, expected)

if __name__ == '__main__':
    unittest.main()
