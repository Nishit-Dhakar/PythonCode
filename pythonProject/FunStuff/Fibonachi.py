ctr = int(input("How many number you want to view in Fibonachi Series"))

def fibo(ctr):
    currentNum, previousNum = 1, 0
    newVal = 0
    if ctr ==1:
        print(ctr)
    else:
        print(previousNum, end= " ")
        print(currentNum, end=" ")
        for i in range(2,ctr):
            newVal = currentNum + previousNum
            previousNum = currentNum
            currentNum = newVal
            print(newVal, end=" ")


fibo(ctr)