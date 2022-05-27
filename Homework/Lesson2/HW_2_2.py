# Перестановка чисел

a = int(input('Введите трехзначное положительное целое число: '))

number_1 = a // 100
number_2 = a % 100 // 10
number_3 = a % 10

print('Результат: ', number_3 * 100 + number_2 * 10 + number_1)




