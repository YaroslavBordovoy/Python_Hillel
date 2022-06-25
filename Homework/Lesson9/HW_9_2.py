# Степень числа

number = int(input('Enter a number: '))

num = 2
# Result with loop

def degree(num, number):
    result = 1
    while number > 0:
        result *= num
        number -= 1
    while number < 0:
        result /= num
        number += 1
    return result

print('Result with loop: ', degree(num, number))

# Result with recursion

def degree(num, number):
    if number == 0:
        return 1
    elif number < 0:
        return 1 / degree(num, -number)
    elif number % 2 == 0:
        return degree(num, number // 2) * degree(num, number // 2)
    else:
        return degree(num, number-1)*num

print('Result with recursion: ', degree(num, number))
