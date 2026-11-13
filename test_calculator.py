import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-2, -3), -5)
        self.assertAlmostEqual(add(1.5, 2.5), 4.0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(-1, -1), 0)
        self.assertAlmostEqual(subtract(2.5, 1.5), 1.0)
    # ##########################

    ######## Partner 1
    def test_multiply(self):  # 3 assertions
        self.assertEqual(mul(0, 2), 0)
        self.assertEqual(mul(0, 0), 0)
        self.assertEqual(mul(10, -10), -100)

    def test_divide(self):  # 3 assertions
        self.assertEqual(div(2, 2), 1)
        self.assertEqual(div(2, 0), 0)
        self.assertEqual(div(10, -10), -1)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self):
        # div(a, b) returns b / a, so the ZeroDivisionError is triggered when a == 0
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)
        with self.assertRaises(ZeroDivisionError):
            div(0, 0)
        with self.assertRaises(ZeroDivisionError):
            div(0, -3)

    def test_logarithm(self):
        # log(a, b) is log base a of b
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(10, 100), 2)
        self.assertAlmostEqual(logarithm(10, 1000), 3)
        self.assertAlmostEqual(logarithm(5, 1), 0)
        self.assertAlmostEqual(logarithm(2, 0.5), -1)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(1, 5)  # base of 1
        with self.assertRaises(ValueError):
            logarithm(0, 5)  # base of 0
        with self.assertRaises(ValueError):
            logarithm(-2, 5)  # negative base
        with self.assertRaises(ValueError):
            logarithm(2, 0)  # b must be positive
        with self.assertRaises(ValueError):
            logarithm(2, -8)  # negative argument
    # ##########################

    ######## Partner 1
    def test_log_invalid_argument(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(4, -4)

    def test_hypotenuse(self):  # 3 assertions
        self.assertEqual(hypotenuse(5, 12), 13)
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertNotEqual(hypotenuse(10, 10), 10)

    def test_sqrt(self):  # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-3)
            square_root(4)
            square_root(30)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
