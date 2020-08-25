from functools import reduce

def square(arg):
    return arg * arg

result = square(10)
print(result)

f= lambda a:a*a
result = f(20)
print(result)

#Example of Filter(), map and reduce
lst = [1,2,3,4,5,6,7,7,8,9,99,22,44]
even = list(filter(lambda n:n%2==0,lst))
doubles = list(map(lambda n:n*2,even))
#multiple inputs to lambda to add all values in doubles
limitVal = reduce(lambda a,b:a+b,doubles)

print(even)
print(doubles)
print(limitVal)
