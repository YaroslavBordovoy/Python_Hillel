# Числа фиббоначи

number = int(input('Enter a number: '))

# Result with loop

num1 = 0
num2 = 1

if number == 0:
    print("Result with loop: F(" + str(number) + ") =", number)
elif number == 1:
    print("Result with loop: F(" + str(number) + ") =", number)
else:
    print('Fibonacci series: ', num1, num2, end=" ")
    for i in range(2, number + 1):
        num1, num2 = num2, num1 + num2
        print(num2, end = " ")
    print("Result with loop: F(" + str(number) + ") =", num2)

# Result with recursion

def recursion(number):
    if number == 0:
        return 0
    else:
        return 1 if number in (1, 2) else recursion(number - 1) + recursion(number - 2)

print("Result with recursion: F(" + str(number) + ") =", recursion(number))