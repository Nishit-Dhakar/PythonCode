from numpy import *

#deep using copy() function vs
# Alliasing arr1= arr2
#shadow copy using view()
arr1 = array([1,2,3,4,5],int)
arr2 = arr1.copy()
print(arr2, end=" ")
print(id(arr2))
print (id(arr1))
#Concatinate 2 arrays directly
arr1 = array([1,2,3,4,5],int)
arr2 = array([6,2,3,4,5],int)
arr = concatenate([arr1,arr2])
print(arr)


#Sin, Cos, Log, Tan, sqrt,sum
arr1 = array([1,2,3,4,5],int)
print(sin(arr1))
print(min(arr1))
print(sum(arr1))

#Add 2 arrays directly
arr1 = array([1,2,3,4,5],int)
arr2 = array([6,2,3,4,5],int)
arr = arr1+arr2
print(arr)

#Add number directly to all items
arr = array([1,2,3,4,5],int)
arr = arr+5
print(arr)