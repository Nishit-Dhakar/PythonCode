
pos = -1

#In case of binary search, values need to be sorted
def search(lst,val):
    lower = 0
    upper = len(lst)
    mid = int((lower+upper)/2)
    for i in range(len(lst)):
        if lst[mid] == val:
            globals()["pos"] = mid
            break
        else:
            if lst[mid] < val:
                lower = mid
                mid = int((lower+upper)/2)
            else:
                upper = mid
                mid = int((lower+upper)/2)


lst = [100,2,3,4,5,6,7,8,89,9]
lst.sort()

print(lst)

search(lst,9)
if pos == -1:
    print("Value not found")
else:
    print("Found item at {}".format(pos))