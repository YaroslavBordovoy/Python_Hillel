# Срезы строки

string = input('Enter a string: ')

# Все символы с четным индексом в строке (индексация начинается с 0)

print('Even indexes: ', string[::2])

# Все символы с нечетным индексом

print('Odd indexes: ', string[1::2])

# Пятый символ в строке, если он есть (если строка не слишком короткая)

if len(string) <= 4:
    print('Fifth character: less than five characters in string!')
else:
    print('Fifth character: ', string[4])

"""
Пришлось задать условие, так как в pycharm`е выбивает ошибку
если в строке меньше 5 символов
"""

# Все до десятого символа

print('All up to the tenth character: ', string[:10])

# Последние 5 символов строки

print('Last five characters: ', string[-5:])

# Строку в обратном порядке

print('Reverse order: ', string[::-1])

# Строку в обратном порядке через один символ (с увеличенным шагом)

print('Reverse order through one character: ', string[::-2])

# Длина строки

print('String length: ', len(string))

# Палиндром

if string == string[::-1]:
    print('Is a palindrome')
else:
    print('Is not a palindrome')