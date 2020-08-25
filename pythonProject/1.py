x = int(input("how many candies you want?"))
def fun(ctr):
    print ("Candies", ctr)

ctr = 1
while ctr <= x:
    fun(ctr);
    ctr+=1

for j in range(4):
    for i in range(4-j):
        print("$", end="")
    print()
