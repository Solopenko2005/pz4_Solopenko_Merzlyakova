"""
basic_math.py
Базовый модуль для математических операций с числами.
Содержит класс NumberCalculator с основными арифметическими действиями.
"""

import math
from typing import Union, List

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


# Пример использования
if __name__ == "__main__":
    calc = NumberCalculator([1, 2, 3, 4])
    print("Сумма списка:", calc.sum_list())
    print("Произведение списка:", calc.product_list())
    print("5 + 3 =", calc.add(5, 3))
    print("10 / 2 =", calc.divide(10, 2))
    print("Факториал 5 =", calc.factorial(5))