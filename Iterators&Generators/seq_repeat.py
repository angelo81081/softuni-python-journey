class sequence_repeat():
    def __init__(self, seq, num):
        self.seq = seq
        self.num = num
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx == self.num:
            raise StopIteration
        result = self.seq[self.idx % len(self.seq)]
        self.idx += 1
        return result


result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')
