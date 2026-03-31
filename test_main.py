# Ячейка 3: ЗАПУСК ТЕСТОВ

import unittest
import sys

sys.path.append('.')

import test_basic_math

loader = unittest.TestLoader()
suite = loader.loadTestsFromModule(test_basic_math)
runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)

print("\n" + "="*60)
if result.wasSuccessful():
    print("✅ ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО!")
    print(f"   Выполнено тестов: {result.testsRun}")
    print(f"   Ошибок: 0")
    print(f"   Провалов: 0")
else:
    print("❌ НЕКОТОРЫЕ ТЕСТЫ НЕ ПРОЙДЕНЫ!")
    print(f"   Выполнено тестов: {result.testsRun}")
    print(f"   Ошибок: {len(result.errors)}")
    print(f"   Провалов: {len(result.failures)}")
print("="*60)
