class vowels:
    def __init__(self, text: str) -> None:
        self.text = text
        self.vowels = ['a', 'e', 'i', 'o', 'u']
        self.vowels_text = [x for x in self.text if x.lower() in self.vowels]
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.vowels_text) - 1:
            self.index += 1
            return self.vowels_text[self.index]

        else:
            self.index = -1
            raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
