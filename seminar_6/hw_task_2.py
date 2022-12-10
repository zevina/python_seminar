# 2.	Орел и решка
#
# Дана строка текста, состоящая из букв русского алфавита "О" и "Р".
# Буква "О" – соответствует выпадению Орла, а буква "Р" – соответствует выпадению Решки.
# Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.
#
# Формат входных данных:
# На вход программе подается строка текста, состоящая из букв русского алфавита "О" и "Р".
#
# Формат выходных данных:
# Программа должна вывести наибольшее количество подряд выпавших Решек.
#
# Примечание. Если выпавших Решек нет, то необходимо вывести число 0.
#
# Входные данные
# ОРРОРОРООРРРО
# ООООООРРРОРОРРРРРРР
# ООООРРРРОРОРРРРРРРРООРОРОРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРР
#
# Выходные данные
# 3
# 7
# 31

import re

s = 'ООООРРРРОРОРРРРРРРРООРОРОРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРР'
print('Входные данные:', s)
rle = []
count = 0

for i in range(0, len(s) - 1):
    if s[i] == s[i + 1]:
        count += 1
    elif s[i] != s[i + 1]:
        count += 1
        rle.append(count)
        rle.append(s[i])
        count = 0
    if i == (len(s) - 2) and s[-2] != s[-1]:
        rle.append(1)
        rle.append(s[i])
    elif i == (len(s) - 2) and s[-2] == s[-1]:
        count += 1
        rle.append(count)
        rle.append(s[i])

st = ''
for el in rle:
    st += str(el)

# print('Текст после кодировки:', st)

sp2 = []
for i in range(len(st)):
    if st[i].isalpha():
        sp2.append(st[i])

rep = re.compile("[^0-9,\d]")
st = rep.sub(" ", st)
sp1 = st.split()
for i in range(len(sp1)):
    sp1[i] = int(sp1[i])

res = list(zip(sp1, sp2))
res = list(filter(lambda x: 'Р' in x[1], res))

if res:
    res = list(zip(*res))
    max_n = max(res[0])
    print('Наибольшее количество подряд выпавших Решек:', max_n)
else:
    print(0)
