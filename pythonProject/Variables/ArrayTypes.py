from numpy import *

#zeros
arr = zeros(10, int)
print(arr)

#logspace
arr = logspace(1,40,5)
print(arr)
print("%.2f" %arr[4])

#arange
arr = arange(1,10,5)
print(arr)

#linspace
arr = linspace(0,15,16)
print(arr)

#array
arr = array([1,2,3,4,5.2,6])
print(arr)
print(arr.dtype)
