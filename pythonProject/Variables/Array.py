from array import *

arr = array("f",[-1.2,1,2,3,4,7,8.9])
print(arr[0])
arr.reverse()
print(arr[0])

print (arr.buffer_info())
print (arr.typecode)

for i in range(len(arr)):
    print(arr[i])

for e in arr:
    print(e)
# Copy from one array to another array
newArr = array(arr.typecode,(a for a in arr))
for e in newArr:
    print(e)
#Square of number in new array
newArr = array(arr.typecode,(a*a for a in arr))
for e in newArr:
    print(e)


#program to ask user to fill Array
arrlen = int(input("Enter Length of Array"))
userArr = array("i",[])

for i in range(arrlen):
    x = int(input("Enter the next value # "))
    userArr.append(x)

for e in userArr:
    print(e, end=" ")
print()

x = int(input("What do you want to search in Array"))
for i in userArr:
    if i == x:
        print("You have entered a 3")
        break

