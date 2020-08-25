
pos = -1

def search(lst,val):
    for i in range(len(lst)):
        if lst[i] == val:
            globals()["pos"] = i
            break

lst = [1,2,3,4,5,6,7,8,89,9]
search(lst,1)
if pos == -1:
    print("Value not found")
else:
    print("Found item at {}".format(pos))