# Подсчет предложений в тексте

string = input('Enter a text: ')

if string[-1] == ('.'):
    print('Number of sentences: ', string.count('.'))
else:
    print('Number of sentences: ', string.count('.') + 1)

