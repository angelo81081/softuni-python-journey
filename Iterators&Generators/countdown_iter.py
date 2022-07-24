class countdown_iterator():
    def __init__(self, count):
        self.count = count
        self.idx = self.count + 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx <= 0:
            raise StopIteration
        self.idx -= 1
        return self.idx


iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")
