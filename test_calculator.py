import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
        def test_add(self):
            self.assertEqual(add(2, 3), 5)
            self.assertEqual(add(-1, 1), 0)
            self.assertEqual(add(0, 0), 0)
            self.assertEqual(add(-2, -3), -5)
            self.assertAlmostEqual(add(1.5, 2.5), 4.0)

        def test_subtract(self):
            self.assertEqual(sub(5, 3), 2)
            self.assertEqual(sub(3, 5), -2)
            self.assertEqual(sub(0, 0), 0)
            self.assertEqual(sub(-1, -1), 0)
            self.assertAlmostEqual(sub(2.5, 1.5), 1.0)

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
            self.assertAlmostEqual(log(2, 8), 3)
            self.assertAlmostEqual(log(10, 100), 2)
            self.assertAlmostEqual(log(10, 1000), 3)
            self.assertAlmostEqual(log(5, 1), 0)
            self.assertAlmostEqual(log(2, 0.5), -1)

        def test_log_invalid_base(self):
            with self.assertRaises(ValueError):
                log(1, 5)  # base of 1
            with self.assertRaises(ValueError):
                log(0, 5)  # base of 0
            with self.assertRaises(ValueError):
                log(-2, 5)  # negative base
            with self.assertRaises(ValueError):
                log(2, 0)  # b must be positive
            with self.assertRaises(ValueError):
                log(2, -8)  # negative argument


# Do not touch this
if __name__ == "__main__":
    unittest.main()