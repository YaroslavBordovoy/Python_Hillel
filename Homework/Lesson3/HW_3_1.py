number = int(input('Enter a number: '))

a = []
k = 0
if number <= 0:
    print('Number is not natural')

elif number >= 0:
    for i in range(2, number + 1):
        k = 0
        for j in range(1, i + 1):
            if i % j == 0:
                k += 1
        if k == 2:
            a.append(i)
    if k == 2:
        print('Number is prime')
    else:
        print('Number is not prime')

    print(a)
