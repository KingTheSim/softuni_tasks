class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.current = 0 - step
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.count:
            self.counter += 1
            self.current += self.step
            return self.current

        else:
            raise StopIteration


numbers = take_skip(10, 5)
for number in numbers:
    print(number)