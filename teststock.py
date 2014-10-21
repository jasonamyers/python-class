import unittest
import io
from unittest.mock import patch, MagicMock
from stock import Stock, read_portfolio

class TestStock(unittest.TestCase):
    def test_create(self):
        s = Stock('GOOG', 100, 490.1)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

    def test_cost(self):
        s = Stock('GOOG', 100, 490.1)
        self.assertEqual(s.cost, 49010)

    def test_sell(self):
        s = Stock('GOOG', 100, 490.1)
        s.sell(50)
        self.assertEqual(s.shares, 50)

    def test_set_shares(self):
        s = Stock('GOOG', 100, 490.1)
        s.shares = 50
        self.assertEqual(s.shares, 50)

    def test_set_price(self):
        s = Stock('GOOG', 100, 490.1)
        s.price = 10.0
        self.assertEqual(s.price, 10.0)

    def test_bad_shares(self):
        s = Stock('GOOG', 100, 490.1)
        with self.assertRaises(TypeError):
            s.shares = 11.2

    def test_bad_price(self):
        s = Stock('GOOG', 100, 490.1)
        with self.assertRaises(TypeError):
            s.price = 'cookies'


if __name__ == '__main__':
    unittest.main()
