# 3.	Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.
#
# Подсказка: можно использовать модуль datetime

import time

def my_random (n):
    str_time = str(time.time())   # генерирует милисекунды
    str_time = str_time.replace('.', '')  # убирает точку
    return int(str_time) % n  # берет заданное количество разрядов

print(my_random(100))