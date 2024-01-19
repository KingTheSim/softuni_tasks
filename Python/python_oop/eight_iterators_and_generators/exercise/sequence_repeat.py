class sequence_repeat:
    def __init__(self, text: str, n: int):
        self.text = text
        self.n = n
        self.cur = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur < self.n - 1:
            self.cur += 1
            return self.text[self.cur % len(self.text)]

        else:
            raise StopIteration

result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')

print()
result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')
