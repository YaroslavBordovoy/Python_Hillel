# Инвертирование словаря

translations = {
    'apple': ['malum', 'pomum', 'popula'],
    'fruit': ['baca', 'bacca', 'popum'],
    'punishment': ['malum', 'multa']
}

inv_dict = {}

for key, value in translations.items():
    value = (*value,)
    # print(key, value)
    # print(type(key), type(value))
    inv_dict[value] = key

print(inv_dict)
