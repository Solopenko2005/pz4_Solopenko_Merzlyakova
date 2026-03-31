"""
basic_math.py
Базовый модуль для математических операций с числами.
Содержит класс NumberCalculator с основными арифметическими действиями.
"""

import math
from typing import Union, List
import statistics

class NumberCalculator:

    def __init__(self, numbers: Union[float, List[float]] = None):
        if numbers is None:
            self.numbers = []
        elif isinstance(numbers, (int, float)):
            self.numbers = [numbers]
        else:
            self.numbers = numbers

    def add(self, a: float, b: float) -> float:
        """Сложение."""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Вычитание."""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Умножение."""
        return a * b

    def divide(self, a: float, b: float) -> float:
        """Деление. Выбрасывает исключение при делении на ноль."""
        if b == 0:
            raise ZeroDivisionError("Деление на ноль не допускается")
        return a / b

    def power(self, base: float, exponent: float) -> float:
        """Возведение в степень."""
        return base ** exponent

    def factorial(self, n: int) -> int:
        """Вычисление факториала целого неотрицательного числа."""
        if n < 0:
            raise ValueError("Факториал определён только для неотрицательных целых чисел")
        return math.factorial(n)

    def sum_list(self) -> float:
        """Сумма всех чисел в списке."""
        return sum(self.numbers)

    def product_list(self) -> float:
        """Произведение всех чисел в списке."""
        result = 1
        for num in self.numbers:
            result *= num
        return result

    def add_number(self, num: float):
        """Добавить число в список."""
        self.numbers.append(num)

    def clear(self):
        """Очистить список чисел."""
        self.numbers.clear()

    def min_list(self) -> float:
        """Минимальное значение в списке."""
        if not self.numbers:
            raise ValueError("Список чисел пуст")
        return min(self.numbers)

    def max_list(self) -> float:
        """Максимальное значение в списке."""
        if not self.numbers:
            raise ValueError("Список чисел пуст")
        return max(self.numbers)

    def mean(self) -> float:
        """Среднее арифметическое списка."""
        if not self.numbers:
            raise ValueError("Список чисел пуст")
        return sum(self.numbers) / len(self.numbers)

    def median(self) -> float:
        """Медиана списка."""
        if not self.numbers:
            raise ValueError("Список чисел пуст")
        return statistics.median(self.numbers)

    def mode(self) -> List[float]:
        """Мода (наиболее часто встречающиеся значения) списка."""
        if not self.numbers:
            raise ValueError("Список чисел пуст")
        return statistics.multimode(self.numbers)

    def variance(self, population: bool = True) -> float:
        """
        Дисперсия списка чисел.
        :param population: если True — генеральная дисперсия, иначе выборочная.
        """
        if not self.numbers:
            raise ValueError("Список чисел пуст")
        if population:
            return statistics.pvariance(self.numbers)
        else:
            return statistics.variance(self.numbers)

    def std_dev(self, population: bool = True) -> float:
        """Стандартное отклонение."""
        return math.sqrt(self.variance(population))

    @staticmethod
    def gcd(a: int, b: int) -> int:
        """Наибольший общий делитель двух целых чисел."""
        return math.gcd(a, b)

    @staticmethod
    def lcm(a: int, b: int) -> int:
        """Наименьшее общее кратное двух целых чисел."""
        return abs(a * b) // math.gcd(a, b)

    @staticmethod
    def is_prime(n: int) -> bool:
        """Проверка, является ли число простым."""
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
        """
        Генерирует арифметическую прогрессию.
        :param start: первый член
        :param diff: разность
        :param count: количество членов (неотрицательное)
        :return: список из count членов прогрессии
        """
        if count <= 0:
            return []
        return [start + i * diff for i in range(count)]

    @staticmethod
    def geometric_sequence(start: float, ratio: float, count: int) -> List[float]:
        """
        Генерирует геометрическую прогрессию.
        :param start: первый член
        :param ratio: знаменатель
        :param count: количество членов (неотрицательное)
        :return: список из count членов прогрессии
        """
        if count <= 0:
            return []
        return [start * (ratio ** i) for i in range(count)]

    def stats_report(self) -> str:
        """Формирует отчёт по статистике текущего списка чисел."""
        if not self.numbers:
            return "Нет данных для статистики."
        return (
            f"Количество чисел: {len(self.numbers)}\n"
            f"Сумма: {self.sum_list()}\n"
            f"Среднее: {self.mean():.4f}\n"
            f"Медиана: {self.median():.4f}\n"
            f"Мода: {self.mode()}\n"
            f"Дисперсия (генер.): {self.variance(population=True):.4f}\n"
            f"Ст. отклонение (генер.): {self.std_dev(population=True):.4f}\n"
            f"Минимум: {self.min_list()}\n"
            f"Максимум: {self.max_list()}"
        )


# Пример использования
if __name__ == "__main__":
    calc = NumberCalculator([1, 2, 3, 4, 5, 5, 6])
    print("Сумма списка:", calc.sum_list())
    print("Произведение списка:", calc.product_list())
    print("5 + 3 =", calc.add(5, 3))
    print("10 / 2 =", calc.divide(10, 2))
    print("Факториал 5 =", calc.factorial(5))
    print("\n--- Статистический отчёт ---")
    print(calc.stats_report())
    print("\n--- Прогрессии ---")
    print("Арифметическая (начало=1, разность=2, кол-во=5):", calc.arithmetic_sequence(1, 2, 5))
    print("Геометрическая (начало=2, знаменатель=3, кол-во=4):", calc.geometric_sequence(2, 3, 4))
    print("\n--- Теория чисел ---")
    print("НОД(48, 18):", calc.gcd(48, 18))
    print("НОК(48, 18):", calc.lcm(48, 18))
    print("17 простое?", calc.is_prime(17))
    print("20 простое?", calc.is_prime(20))