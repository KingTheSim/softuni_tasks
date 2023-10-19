class custom_range:
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end
        self.result = self.start - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.result < self.end:
            self.result += 1
            return self.result

        else:
            self.result = self.start
            raise StopIteration


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)
