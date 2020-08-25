lst = [2,3,4,5,6,7]

itr = iter(lst)
# print(itr.__next__())
# print(next(itr))

class top10val:
    def __init__(self):
        self.num=1

    def __iter__(self):
        return self;
    def __next__(self):
        if self.num > 10:
            raise StopIteration
        else:
            val = self.num
            self.num= self.num +1
            return val

a = top10val()
print(a.__next__())
for i in a:
    print(i)