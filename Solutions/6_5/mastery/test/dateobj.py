# test/dateobj.py

import unittest
from .. import dateobj

class TestDate(unittest.TestCase):
    def test_create(self):
        d = dateobj.Date(2014, 6, 1)
        self.assertEqual(d.year, 2014)
        self.assertEqual(d.month, 6)
        self.assertEqual(d.day, 1)

if __name__ == '__main__':
    unittest.main()
