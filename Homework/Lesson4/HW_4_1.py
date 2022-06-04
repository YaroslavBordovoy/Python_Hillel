# Замена символов в строке

string = input('Enter your string: ')

str_2 = string[string.find(' '):string.rfind(' ')]
str_3 = str_2.replace('n', 'N')
str_4 = string[:string.find(' ')] + str_3 + string[string.rfind(' '):]

print('Your string: ', str_4)