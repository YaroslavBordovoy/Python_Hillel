# Перестановка чисел

a = int(input('Введите трехзначное положительное целое число: '))

number_1 = a % 10
number_2 = (a // 10) % 10
number_3 = (a // 100 ) % 10

result = str(number_1) + str(number_2) + str(number_3)

print('Результат:', result)