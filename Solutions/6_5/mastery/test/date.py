# test/date.py

import unittest
from .. import date

class TestDate(unittest.TestCase):
    def self_create(self):
        d = unittest.Date(2014, 6, 1)
        self.assertEqual(d.year, 2014)
        self.assertEqual(d.month, 6)
        self.assertEqual(d.day, 1)

if __name__ == '__main__':
    unittest.main()
