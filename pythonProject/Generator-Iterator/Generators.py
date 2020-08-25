lst = [2,3,4,5,6,7]

itr = iter(lst)
# print(itr.__next__())
# print(next(itr))

def topvals(a):
    num = 1
    while num <=a:
        yield (num*num)
        num+= 1

# value = topvals()
# print(value.__next__())
val = topvals(10)
for i in val:
    print(i)