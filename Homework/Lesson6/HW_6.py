# Уникальные имена

# Ваня Коля Маша Дима Женя Коля Дима Маша

name_list = input('Enter a names: ').strip().split()

l1 = []
l2 = []

for name in name_list:
    if name not in l1:
        l1.append(name)
    elif name in l1:
        l2.append(name)

set_1 = set(l1)
set_2 = set(l2)

print('Non-Duplicate Names: ', *set_1 - set_2)