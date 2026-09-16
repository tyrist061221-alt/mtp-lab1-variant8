"""Модульные тесты для main.py (запуск: python -m unittest discover -s tests)."""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import main  # noqa: E402


class TestCalculator(unittest.TestCase):
    """Проверка функций арифметики."""

    def test_add(self):
        self.assertEqual(main.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(main.subtract(10, 4), 6)

    def test_multiply(self):
        self.assertEqual(main.multiply(3, 4), 12)

    def test_divide(self):
        self.assertEqual(main.divide(9, 3), 3)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            main.divide(1, 0)

    def test_power(self):
        self.assertEqual(main.power(2, 10), 1024)

    def test_factorial(self):
        self.assertEqual(main.factorial(5), 120)

    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            main.factorial(-1)


if __name__ == "__main__":
    unittest.main()
