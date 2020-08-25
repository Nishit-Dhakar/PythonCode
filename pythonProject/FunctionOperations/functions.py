from numpy import *

#function flexible arguments with keywords
def fmailyageCalc(a,**arg):
    print (arg)
    for i,j in arg.items():
        print(i,j)

fmailyageCalc(0, nishitage=38,roopamage=38,aruage=12)
#function flexible arguments
def addition(a,*arg):
    sum = a;
    for i in arg:
        sum = sum +i
    print (sum)

#addition(2,3,4,5,6);

#function operations
def person(name, age=21):
    print(name,end=" ")
    print(age-1)

# person("nishit",37)
# person(age=37,name="nishit")
# person(name="nishit")

# Function to do Array operations
def flattenArray(arg):
    x = arg.flatten()
    print(x)
    print(arg.sum())
    print(arg.reshape(4,2))

arr = array([
    [1,2,3,4],
    [5,6,7,8]
])

#flattenArray(arr);

def add(arg1, arg2):
    x= (arg1 + arg2)
    y = (arg1 * arg2)
    return x,y

def greet():
    print("Hello")
    print("Good morning - Nishit Dhakar")



# greet();
#
# x = int(input("Enter first value for addition"))
# y = int(input("Enter Second value for addition"))
# a,b = add(x,y);
# print(a)
# print(b)

