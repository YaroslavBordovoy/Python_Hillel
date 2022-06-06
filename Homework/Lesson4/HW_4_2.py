# Подсчет предложений в тексте

string = input('Enter a text: ')

if string == (''):
    print('You did not enter a string')
elif string[-1] == ('.'):
    print('Number of sentences: ', string.count('.'))
else:
    print('Number of sentences: ', string.count('.') + 1)

