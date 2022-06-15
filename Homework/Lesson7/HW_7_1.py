text = input('Enter the text: ')

import string
for c in string.punctuation:
    if c in text:
        text = text.replace(c, '')

t1 = text.lower()
words = t1.split()

count = {}

for element in words:
    if count.get(element, None):
        count[element] += 1
    else:
        count[element] = 1

sorted_dict = sorted(count.items(), key = lambda a: a[1], reverse = True)

print('Complete list of words: ', sorted_dict)
print('Top 5 words: ', sorted_dict[:5])