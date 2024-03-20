import unittest
from fraction import *

class TestFractionMethods(unittest.TestCase):
    def test_init(self):
        self.assertEqual(Fraction(1, 2).num, 1)
        self.assertEqual(Fraction(1, 2).den, 2)
        with self.assertRaises(ValueError):
            Fraction(1, 0)
    def test_str(self):
        self.assertEqual(str(Fraction(1, 2)), "(1 / 2)")
        self.assertEqual(str(Fraction(2, 4)), "(2 / 4)")
    def test_add(self):
        self.assertEqual(Fraction(1, 2) + (Fraction(1, 3)), Fraction(5, 6))
    def test_mul(self):
        self.assertEqual(Fraction(1, 2) * (Fraction(1, 3)), Fraction(1, 6))
    def test_eq(self):
        self.assertEqual(Fraction(2, 4), Fraction(1, 2))
    def test_simplify(self):
        self.assertEqual(Fraction(2, 4).simplify(), Fraction(1, 2))

if __name__ == '__main__':
    unittest.main()