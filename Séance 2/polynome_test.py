import unittest
from polynome import *

class TestPolynomeMethods(unittest.TestCase):
    def test_init(self):
        self.assertEqual(Polynomial([1, 2, 3]).coefs, [1, 2, 3])
    def test_add(self):
        self.assertEqual(Polynomial([1, 2, 3]) + (Polynomial([1, 2, 3])), Polynomial([2, 4, 6]))
    def test_derivative(self):
        self.assertEqual(Polynomial([1, 2, 3]).derivative(), Polynomial([2, 6]))
    def test_integrate(self):
        self.assertEqual(Polynomial([1, 2, 3]).integrate(), Polynomial([0, 1, 1, 1]))