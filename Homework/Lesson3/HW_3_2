count = 0
sum = 0
max = None
min = None
average = 0

while True:
    n = input('Enter a number: ')
    if not n:
        print('count: ' + str(count))
        print('sum: ' + str(sum))
        print('max: ' + str(max))
        print('min: ' + str(min))
        print('average: ' + str(average))
        break
    number = int(n)
    count += 1
    sum += number
    if max is None or number > max:
        max = number
    if min is None or number < min:
        min = number
    average = sum / count