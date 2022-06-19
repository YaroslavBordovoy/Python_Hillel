# Поиск квадратного корня

number = int(input("Enter a number: "))

def find_the_square_root(number):
    if number == 0 or number == 1:
        return number

    start = 1
    end = number
    while start <= end:
        mid = (start + end) // 2
        if mid * mid == number:
            return mid
        elif mid * mid < number:
            start = mid + 1
            n = mid
        else:
            end = mid - 1
    return n

print('The square root of a', number, 'is', find_the_square_root(number))