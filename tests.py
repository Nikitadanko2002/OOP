import unittest
from complex import TComplex

class TComplexTests(unittest.TestCase):
    def test_addition(self):
        complex1 = TComplex(2, 3)
        complex2 = TComplex(1, 4)
        result = complex1 + complex2
        self.assertEqual(result, TComplex(3, 7))

    def test_subtraction(self):
        complex1 = TComplex(5, 6)
        complex2 = TComplex(2, 3)
        result = complex1 - complex2
        self.assertEqual(result, TComplex(3, 3))

    def test_multiplication(self):
        complex1 = TComplex(2, 3)
        complex2 = TComplex(4, 5)
        result = complex1 * complex2
        self.assertEqual(result, TComplex(-7, 22))

    def test_division(self):
        complex_1 = TComplex(5, 3)
        complex_2 = TComplex(2, -2)
        result = complex_1 / complex_2
        self.assertEqual(result, TComplex(0.5, 2.0))
