# Соседние числа

import random

n = int(input('Enter a number to generate a list: '))


list = [random.randint(0, n) for i in range(n // 2)]
print(list)

number = int(input('Number: '))

for i, v in enumerate(list):
    if number not in list:
        print('Sorry')
        break
    elif number == list[0]:
        # print('001', i, v)
        print('Right: ', list[i + 1])
        break
    elif number == v and number != list[-1]:
        # print('002', i, v)
        print('Left: ', list[i - 1], 'Right: ', list[i + 1])
        break
    elif number == v and number == list[-1]:
        # print('003', i, v)
        print('Left: ', list[i - 1])
        break