
def bubbleSort(lst):
    for i in range(len(lst)-1,0,-1):
        for j in range(i):
            if(lst[i] < lst[j]):
                #lst[i],lst[j] = lst[j],lst[i]
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp


lst = [100,2,3,4,5,6,7,8,89,9]
bubbleSort(lst)

print(lst)