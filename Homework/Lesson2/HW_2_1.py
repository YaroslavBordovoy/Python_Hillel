# Закрепление операторов деления

a = int(input('Количество детей в первой группе: '))
b = int(input('Количество детей во второй группе: '))

# group 1

c = (a // 2) + (a % 2)

# group 2

d = (b // 2) + (b % 2)

# total

total = c + d

print('Нужное количество кроватей:', total)