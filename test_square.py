from square import area, perimeter

import unittest

class SquareTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_mul1(self):
        res = area(3)
        self.assertEqual(res, 9)
        
    def test_mul2(self):
        res = area(-9)
        self.assertEqual(res, 0)

    def test_add1(self):
        res = perimeter(3)
        self.assertEqual(res, 12)

    def test_add2(self):
        res = perimeter(-8)
        self.assertEqual(res, 0)