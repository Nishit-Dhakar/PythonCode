
ctr = int(input("Enter # whose factorial you want - "))
counter = 1
finalVal = 1

def recursiveFun(arg):
    global finalVal
    global ctr
    if(arg == counter):
        finalVal = finalVal * counter
    else:
        finalVal = finalVal * ctr
        ctr = ctr-1
        recursiveFun(ctr)

recursiveFun(ctr)
print("Factorial is {}".format(finalVal))