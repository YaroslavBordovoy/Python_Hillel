# Запись в файл

r = open('Text.txt', 'w')

while True:
    n = input('Enter text to write: ')
    r.write(n + '\n')
    if not n:
        break

r.close()
print('File writing finished')

r = open('Text.txt')
print('-------------------', '\n' + r.read())
r.close()
