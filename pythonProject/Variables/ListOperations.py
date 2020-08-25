lst = [1,21,35,5,6,73,8,94,0]
lst2 = ["nishit","aryaa","roopam"]

# Combine 2 list
# lst3 = lst +lst2
# print(lst3)

#read values 1 by 1
# lst.sort()
# for i in lst:
#     print(i)
# i=0
# while i < len(lst):
#     print(lst[i])
#     i = i + 1
def listoperations():
        try:
                val = int(input("Enter your list length - "))
                lst3 = []
                for i in range(val):
                    temp = int(input("Enter value {} -".format(i)))
                    lst3.append(temp)

                print(lst3)

                # Sorting descending
                for i in range(len(lst3)-1,0,-1):
                    for j in range(i):
                        if lst3[i]>lst3[j]:
                            temp = lst3[i]
                            lst3[i]= lst3[j]
                            lst3[j] = temp
                print(lst3)

        except Exception as e:
                print("sir, please enter integers Only else tata")
                listoperations()

listoperations()

