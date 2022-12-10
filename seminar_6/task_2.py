# 2.	На первой строке вводится натуральное число N — количество строк.
# Далее следуют N строк, которые надо будет отсортировать
#
# Ввод
# 4
# три
# четыре
# пять
# шесть
#
# Вывод
# три
# пять
# шесть
# четыре

n = int(input('Введите количество строк: '))
sp = []

for i in range(n):
    x = input()
    sp.append(x)

sp.sort(key=lambda v: len(v))
print('Строки, отсортированные по длине: ')
for el in sp:
    print(el)