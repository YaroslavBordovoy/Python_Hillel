# Сумма двух чисел

import random

n = int(input('Enter a number to generate a list: '))

list = [random.randint(0, n) for i in range(n // 2)]
print(list)

number = int(input('Enter a number: '))

fl = False
for i in range(len(list)):
    if fl:
        break
    for j in range(i + 1, len(list)):
        if list[i] + list[j] == number:
            print('First index: ', i, 'Second index: ', j)
            fl = True
            break