# Ячейка 2: СОЗДАНИЕ ТЕСТОВ

test_code = '''
import unittest
import math
from basic_math import NumberCalculator

class TestNumberCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = NumberCalculator([1, 2, 3, 4, 5, 5, 6])
        self.empty_calc = NumberCalculator()

    def test_add(self):
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(5, -3), 2)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)
        self.assertEqual(self.calc.subtract(-10, -4), -6)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(6, 7), 42)
        self.assertEqual(self.calc.multiply(10, 0), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)

    def test_power(self):
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 0), 1)

    def test_factorial(self):
        self.assertEqual(self.calc.factorial(5), 120)
        self.assertEqual(self.calc.factorial(0), 1)
        with self.assertRaises(ValueError):
            self.calc.factorial(-5)

    def test_sum_list(self):
        self.assertEqual(self.calc.sum_list(), 26)
        self.assertEqual(self.empty_calc.sum_list(), 0)

    def test_product_list(self):
        self.assertEqual(self.calc.product_list(), 3600)
        self.assertEqual(self.empty_calc.product_list(), 1)

    def test_add_number(self):
        self.calc.add_number(10)
        self.assertEqual(len(self.calc.numbers), 8)
        self.assertEqual(self.calc.numbers[-1], 10)

    def test_clear(self):
        self.calc.clear()
        self.assertEqual(len(self.calc.numbers), 0)

    def test_min_list(self):
        self.assertEqual(self.calc.min_list(), 1)
        with self.assertRaises(ValueError):
            self.empty_calc.min_list()

    def test_max_list(self):
        self.assertEqual(self.calc.max_list(), 6)
        with self.assertRaises(ValueError):
            self.empty_calc.max_list()

    def test_mean(self):
        self.assertAlmostEqual(self.calc.mean(), 26/7, places=2)
        with self.assertRaises(ValueError):
            self.empty_calc.mean()

    def test_median(self):
        self.assertEqual(self.calc.median(), 4)

    def test_mode(self):
        self.assertEqual(self.calc.mode(), [5])

    def test_variance(self):
        calc_simple = NumberCalculator([1, 2, 3, 4, 5])
        self.assertAlmostEqual(calc_simple.variance(population=True), 2.0, places=2)
        self.assertAlmostEqual(calc_simple.variance(population=False), 2.5, places=2)

    def test_std_dev(self):
        calc_simple = NumberCalculator([1, 2, 3, 4, 5])
        self.assertAlmostEqual(calc_simple.std_dev(population=True), math.sqrt(2), places=2)

    def test_gcd(self):
        self.assertEqual(NumberCalculator.gcd(48, 18), 6)
        self.assertEqual(NumberCalculator.gcd(10, 0), 10)

    def test_lcm(self):
        self.assertEqual(NumberCalculator.lcm(12, 18), 36)

    def test_is_prime(self):
        self.assertTrue(NumberCalculator.is_prime(17))
        self.assertTrue(NumberCalculator.is_prime(2))
        self.assertFalse(NumberCalculator.is_prime(1))
        self.assertFalse(NumberCalculator.is_prime(4))
        self.assertFalse(NumberCalculator.is_prime(100))

    def test_arithmetic_sequence(self):
        result = NumberCalculator.arithmetic_sequence(1, 2, 5)
        self.assertEqual(result, [1, 3, 5, 7, 9])
        self.assertEqual(NumberCalculator.arithmetic_sequence(1, 2, 0), [])

    def test_geometric_sequence(self):
        result = NumberCalculator.geometric_sequence(2, 3, 4)
        self.assertEqual(result, [2, 6, 18, 54])

    def test_stats_report(self):
        report = self.calc.stats_report()
        self.assertIsInstance(report, str)
        self.assertIn("Количество чисел: 7", report)

    def test_init_with_none(self):
        calc = NumberCalculator(None)
        self.assertEqual(calc.numbers, [])

    def test_init_with_single_number(self):
        calc = NumberCalculator(42)
        self.assertEqual(calc.numbers, [42])

    def test_init_with_list(self):
        calc = NumberCalculator([1, 2, 3])
        self.assertEqual(calc.numbers, [1, 2, 3])

if __name__ == "__main__":
    unittest.main()
'''

with open('test_basic_math.py', 'w', encoding='utf-8') as f:
    f.write(test_code)

print("✅ Файл test_basic_math.py создан")
