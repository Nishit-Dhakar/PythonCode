from numpy import *

arr = array([
                [5,6,7,3],
                [2,3,4,7]
            ]
           )

arr1 = matrix(arr)
print(arr1)
arr2 = matrix("1 2 ;3 4;2 5 ;6 7")
arr3 = matrix("1 2 ;3 4;2 5 ;6 7")
print(arr2)
print(diagonal(arr2))
print(arr2.max())
print (arr3 + arr2)

arr = array ([
    [5,6,7,3,4,5],
    [2,3,4,7,8,9]]
)

arr1 = arr.flatten()
arr2 = arr1.reshape(3,4)
print(arr1)
print(arr2)
# print(arr.shape)
# print(arr.size)
# print(arr.ndim)
#print(arr.dtype)