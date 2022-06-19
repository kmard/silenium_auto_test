
# python test_3_2_12_unitest.py


import unittest

"""
docs https://docs.python.org/3/library/unittest.html
"""
class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")

    def test_abs2(self):
        self.assertEqual(abs(-42), -42, "Should be absolute value of a number")


if __name__ == "__main__":
    unittest.main()



# Импортировать unittest в файл: import unittest
# Создать класс, который должен наследоваться от класса TestCase: class TestAbs(unittest.TestCase):
# Превратить тестовые функции в методы, добавив ссылку на экземпляр класса self в качестве первого аргумента функции: def test_abs1(self):
# Изменить assert на self.assertEqual()
# Заменить строку запуска программы на unittest.main()
