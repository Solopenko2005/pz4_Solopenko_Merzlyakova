# Ячейка 1: СОЗДАНИЕ МОДУЛЯ basic_math.py (ИСПРАВЛЕННЫЙ)

basic_math_code = '''
import math
import statistics
from typing import Union, List, Tuple

class NumberCalculator:
    """Класс для выполнения основных математических операций."""

    def __init__(self, numbers: Union[float, List[float]] = None):
        if numbers is None:
            self.numbers = []
        elif isinstance(numbers, (int, float)):
            self.numbers = [numbers]
        else:
            self.numbers = numbers

    def add(self, a: float, b: float) -> float:
        return a + b

    def subtract(self, a: float, b: float) -> float:
        return a - b

    def multiply(self, a: float, b: float) -> float:
        return a * b

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Деление на ноль не допускается")
        return a / b

    def power(self, base: float, exponent: float) -> float:
        return base ** exponent

    def factorial(self, n: int) -> int:
        if n < 0:
            raise ValueError("Факториал определён только для неотрицательных целых чисел")
        return math.factorial(n)

    def sum_list(self) -> float:
        return sum(self.numbers)

    def product_list(self) -> float:
        result = 1
        for num in self.numbers:
            result *= num
        return result

    def add_number(self, num: float):
        self.numbers.append(num)

    def clear(self):
        self.numbers.clear()

    def min_list(self) -> float:
        if not self.numbers:
            raise ValueError("Список чисел пуст")
        return min(self.numbers)

    def max_list(self) -> float:
        if not self.numbers:
            raise ValueError("Список чисел пуст")
        return max(self.numbers)

    def mean(self) -> float:
        if not self.numbers:
            raise ValueError("Список чисел пуст")
        return sum(self.numbers) / len(self.numbers)

    def median(self) -> float:
        if not self.numbers:
            raise ValueError("Список чисел пуст")
        return statistics.median(self.numbers)

    def mode(self) -> List[float]:
        if not self.numbers:
            raise ValueError("Список чисел пуст")
        return statistics.multimode(self.numbers)

    def variance(self, population: bool = True) -> float:
        if not self.numbers:
            raise ValueError("Список чисел пуст")
        if population:
            return statistics.pvariance(self.numbers)
        else:
            return statistics.variance(self.numbers)

    def std_dev(self, population: bool = True) -> float:
        return math.sqrt(self.variance(population))

    @staticmethod
    def gcd(a: int, b: int) -> int:
        return math.gcd(a, b)

    @staticmethod
    def lcm(a: int, b: int) -> int:
        return abs(a * b) // math.gcd(a, b)

    @staticmethod
    def is_prime(n: int) -> bool:
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    @staticmethod
    def arithmetic_sequence(start: float, diff: float, count: int) -> List[float]:
        if count <= 0:
            return []
        return [start + i * diff for i in range(count)]

    @staticmethod
    def geometric_sequence(start: float, ratio: float, count: int) -> List[float]:
        if count <= 0:
            return []
        return [start * (ratio ** i) for i in range(count)]

    def stats_report(self) -> str:
        if not self.numbers:
            return "Нет данных для статистики."
        return (
            f"Количество чисел: {len(self.numbers)}\\n"
            f"Сумма: {self.sum_list()}\\n"
            f"Среднее: {self.mean():.4f}\\n"
            f"Медиана: {self.median():.4f}\\n"
            f"Мода: {self.mode()}\\n"
            f"Дисперсия (генер.): {self.variance(population=True):.4f}\\n"
            f"Ст. отклонение (генер.): {self.std_dev(population=True):.4f}\\n"
            f"Минимум: {self.min_list()}\\n"
            f"Максимум: {self.max_list()}"
        )
'''

with open('basic_math.py', 'w', encoding='utf-8') as f:
    f.write(basic_math_code)

print("✅ Файл basic_math.py создан")

# Проверяем импорт
try:
    from basic_math import NumberCalculator
    print("✅ Модуль basic_math импортирован успешно")
except Exception as e:
    print(f"❌ Ошибка импорта: {e}")
