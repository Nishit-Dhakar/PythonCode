
def selectionSort(lst):
    for i in range(0,len(lst)-1,1):
        for j in range(i+1,len(lst),1):
            if(lst[i] > lst[j]):
                #compare first value with j
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp


lst = [100,2,3,4,5,6,7,8,89,9]
selectionSort(lst)

print(lst)