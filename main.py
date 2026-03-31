"""
Модуль обработки данных (Целые числа, строки)
Автор: Студент
Версия: 1.0
Назначение: Поддержка ввода информации, статистическая обработка и фильтрация данных.
"""

import json
import os
from typing import List, Union, Dict, Any

class DataProcessor:
    def __init__(self):
        self.data: List[Union[int, str]] = []

    def input_data(self, interactive: bool = True, input_string: str = None) -> None:
        if interactive:
            print("Введите данные (целые числа или строки).")
            print("Для завершения ввода введите 'stop' или 'exit':")
            while True:
                user_input = input("> ").strip()
                if user_input.lower() in ['stop', 'exit']:
                    break
                self._add_single_value(user_input)
        elif input_string:
            # Парсинг строки вида "10, 20, hello, world, 30"
            parts = [p.strip() for p in input_string.split(',')]
            for part in parts:
                self._add_single_value(part)
            print(f"Загружено {len(parts)} элементов из строки.")

    def _add_single_value(self, value: str) -> None:
        try:
            int_val = int(value)
            self.data.append(int_val)
        except ValueError:
            if value:  # Игнорируем пустые строки
                self.data.append(value)

    def get_numbers(self) -> List[int]:
        return [item for item in self.data if isinstance(item, int)]

    def get_strings(self) -> List[str]:
        return [item for item in self.data if isinstance(item, str)]

    def number_stats(self) -> Dict[str, float]:
        numbers = self.get_numbers()
        if not numbers:
            return {'count': 0, 'sum': 0, 'min': None, 'max': None, 'avg': None}
        return {
            'count': len(numbers),
            'sum': sum(numbers),
            'min': min(numbers),
            'max': max(numbers),
            'avg': sum(numbers) / len(numbers)
        }

    def filter_strings_by_length(self, min_len: int = 3) -> List[str]:
        return [s for s in self.get_strings() if len(s) >= min_len]

    def display(self) -> None:
        print("\n--- Текущие данные ---")
        if not self.data:
            print("Данные отсутствуют.")
            return
        for i, item in enumerate(self.data, 1):
            print(f"{i}. {item} (тип: {'int' if isinstance(item, int) else 'str'})")

    def save_to_file(self, filename: str = "data_export.json") -> None:
        # Для сохранения в JSON преобразуем объекты в сериализуемый формат
        serializable_data = []
        for item in self.data:
            if isinstance(item, int):
                serializable_data.append({"type": "int", "value": item})
            else:
                serializable_data.append({"type": "str", "value": item})

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(serializable_data, f, ensure_ascii=False, indent=4)
        print(f"Данные сохранены в файл: {filename}")

    def load_from_file(self, filename: str = "data_export.json") -> None:
        if not os.path.exists(filename):
            print(f"Файл {filename} не найден.")
            return

        with open(filename, 'r', encoding='utf-8') as f:
            serializable_data = json.load(f)

        self.data = []
        for item in serializable_data:
            if item["type"] == "int":
                self.data.append(item["value"])
            else:
                self.data.append(item["value"])
        print(f"Данные загружены из файла: {filename} ({len(self.data)} элементов)")


def main():
    processor = DataProcessor()

    print("=" * 50)
    print("Программный модуль обработки данных (целые числа и строки)")
    print("=" * 50)

    # Пример 1: Интерактивный ввод
    print("\n1. Интерактивный ввод данных:")
    processor.input_data(interactive=True)

    # Пример 2: Статистика
    print("\n2. Статистика по числам:")
    stats = processor.number_stats()
    for key, value in stats.items():
        print(f"   {key}: {value}")

    # Пример 3: Фильтрация строк
    strings = processor.get_strings()
    if strings:
        print(f"\n3. Строки длиной >= 3 символов:")
        filtered = processor.filter_strings_by_length(3)
        for s in filtered:
            print(f"   - {s}")

    # Пример 4: Отображение и сохранение
    processor.display()
    processor.save_to_file("my_data.json")


if __name__ == "__main__":
    main()