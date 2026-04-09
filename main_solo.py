
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
            if value:
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

    def analyze_text_data(self) -> Dict[str, Any]:
        strings = self.get_strings()

        if not strings:
            return {
                'total_strings': 0,
                'message': 'Нет текстовых данных для анализа'
            }

        longest_string = max(strings, key=len)
        shortest_string = min(strings, key=len)

        avg_length = sum(len(s) for s in strings) / len(strings)

        all_text = ''.join(strings).lower()
        vowels = 'аеёиоуыэюяaeiou'
        consonants = 'бвгджзйклмнпрстфхцчшщъьbcdfghjklmnpqrstvwxyz'

        vowel_count = sum(1 for char in all_text if char in vowels)
        consonant_count = sum(1 for char in all_text if char in consonants)

        letter_freq = {}
        for char in all_text:
            if char.isalpha():
                letter_freq[char] = letter_freq.get(char, 0) + 1

        most_common_letter = max(letter_freq.items(), key=lambda x: x[1]) if letter_freq else ('нет', 0)

        return {
            'total_strings': len(strings),
            'longest_string': longest_string,
            'longest_length': len(longest_string),
            'shortest_string': shortest_string,
            'shortest_length': len(shortest_string),
            'average_length': round(avg_length, 2),
            'total_characters': len(all_text),
            'vowel_count': vowel_count,
            'consonant_count': consonant_count,
            'most_common_letter': most_common_letter[0],
            'most_common_letter_count': most_common_letter[1]
        }

    def display_text_analysis(self) -> None:
        analysis = self.analyze_text_data()

        print("АНАЛИЗ ТЕКСТОВЫХ ДАННЫХ")


        if analysis.get('total_strings', 0) == 0:
            print(analysis.get('message', 'Нет данных для анализа'))
            return

        print(f" Всего строк: {analysis['total_strings']}")
        print(f" Самая длинная строка: '{analysis['longest_string']}' (длина: {analysis['longest_length']})")
        print(f" Самая короткая строка: '{analysis['shortest_string']}' (длина: {analysis['shortest_length']})")
        print(f" Средняя длина строки: {analysis['average_length']} символов")
        print(f" Всего символов: {analysis['total_characters']}")
        print(f" Гласных букв: {analysis['vowel_count']}")
        print(f" Согласных букв: {analysis['consonant_count']}")
        print(f" Самая частая буква: '{analysis['most_common_letter']}' (встречается {analysis['most_common_letter_count']} раз)")

    def display(self) -> None:

        print("\nТекущие данные")
        if not self.data:
            print("Данные отсутствуют.")
            return
        for i, item in enumerate(self.data, 1):
            print(f"{i}. {item} (тип: {'int' if isinstance(item, int) else 'str'})")

    def save_to_file(self, filename: str = "data_export.json") -> None:
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

    print("Программный модуль обработки данных (целые числа и строки)")
    print("Версия 1.1 - с анализом текстовых данных")


    print("\n1. Интерактивный ввод данных:")
    print("   (Введите числа и строки, для завершения введите 'stop')")
    processor.input_data(interactive=True)

    if not processor.data:
        print("\n⚠️ Данные не введены. Использую тестовые данные для демонстрации.")
        test_data = "10, 25, 42, Python, программирование, тест, 100, hello, мир"
        processor.input_data(interactive=False, input_string=test_data)

    print("\n2. СТАТИСТИКА ПО ЧИСЛАМ:")
    stats = processor.number_stats()
    for key, value in stats.items():
        if value is not None:
            if key == 'avg':
                print(f"   {key}: {value:.2f}")
            else:
                print(f"   {key}: {value}")

    strings = processor.get_strings()
    if strings:
        print(f"\n3. ФИЛЬТРАЦИЯ СТРОК (длина >= 3 символов):")
        filtered = processor.filter_strings_by_length(3)
        if filtered:
            for s in filtered:
                print(f"   ✓ {s} (длина: {len(s)})")
        else:
            print("   Нет строк длиной >= 3 символов")

    print("\n4. АНАЛИЗ ТЕКСТОВЫХ ДАННЫХ:")
    processor.display_text_analysis()

    processor.display()

    print("\n5. СОХРАНЕНИЕ ДАННЫХ:")
    processor.save_to_file("my_data.json")

    print("\n6. ДЕМОНСТРАЦИЯ ЗАГРУЗКИ ДАННЫХ:")
    new_processor = DataProcessor()
    new_processor.load_from_file("my_data.json")
    new_processor.display()

    print("Работа программы завершена")


if __name__ == "__main__":
    main()