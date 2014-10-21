# teststock.py

import stock
import unittest

class TestStock(unittest.TestCase):
    def test_create(self):
        s = stock.Stock('GOOG', 100, 490.1)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)
        
    def test_cost(self):
        s = stock.Stock('GOOG', 100, 490.1)
        self.assertEqual(s.cost, 49010.0)
        
    def test_sell(self):
        s = stock.Stock('GOOG', 100, 490.1)
        s.sell(25)
        self.assertEqual(s.shares, 75)

    def test_shares_good(self):
        s = stock.Stock('GOOG', 100, 490.1)
        s.shares = 50
        self.assertEqual(s.shares, 50)

    def test_shares_bad(self):
        s = stock.Stock('GOOG', 100, 490.1)
        with self.assertRaises(TypeError):
            s.shares = 'a lot'

    def test_price_good(self):
        s = stock.Stock('GOOG', 100, 490.1)
        s.price = 350.25
        self.assertEqual(s.price, 350.25)

    def test_price_bad(self):
        s = stock.Stock('GOOG', 100, 490.1)
        with self.assertRaises(TypeError):
            s.price = 'a lot'

import unittest.mock
import io
class TestReadPortfolio(unittest.TestCase):
    def test_read_portfolio(self):
        with unittest.mock.patch('builtins.open') as m:
            m.return_value = io.StringIO('GOOG 100 490.10\nIBM 50 91.25\n')
            port = stock.read_portfolio('filename')
            self.assertEqual(len(port), 2)
            s = port[0]
            self.assertEqual((s.name, s.shares, s.price), ('GOOG', 100, 490.1))
            s = port[1]
            self.assertEqual((s.name, s.shares, s.price), ('IBM', 50, 91.25))            
if __name__ == '__main__':
    unittest.main()
