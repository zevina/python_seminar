# 7.	Даны два списка чисел. Найдите все числа, которые входят как в первый, так и во второй список
# и выведите их в порядке возрастания.
#
# Входные данные
# 1 3 2
# 4 3 2
#
# Выходные данные
# 2 3

sp_1 = [1, 3, 2]
sp_2 = [4, 3, 2]

a = set(sp_1)
b = set(sp_2)

i = a.intersection(b)
res = list(i)
print(*res)
