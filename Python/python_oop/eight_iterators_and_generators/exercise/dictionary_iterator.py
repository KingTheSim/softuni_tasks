class dictionary_iter:
    def __init__(self, dic: dict):
        self.dic = dic
        self.list_of_items = list(self.dic.items())
        self.counter = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < len(self.dic) - 1:
            self.counter += 1
            return self.list_of_items[self.counter]

        else:
            raise StopIteration


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
 print(x)
