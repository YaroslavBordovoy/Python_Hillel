# Простой счетчик

class Counter:

    current = 0

    def __init__(self, start=None, maximum=None) -> None:
        self.start = start
        self.maximum = maximum
        self.current = start

    def increase(self):
        if self.current < self.maximum:
            self.current += 1
            return self.current
        else:
            return 'Out of range'

    def __repr__(self) -> str:
        return f'Counter(start={self.start}, max={self.maximum}), current position: {self.current}'


start = int(input('Specify initial value: '))
maximum = int(input('Specify end value: '))
my_count = Counter(start=start, maximum=maximum)

while True:
    user_request = input()
    if my_count.current < maximum:
        my_count.increase()
        print(my_count)
    else:
        print('You have reached the maximum value')
