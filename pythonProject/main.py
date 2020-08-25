# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# print('Hello Nishit Dhakar - Welcome to world of Python')
# ch = input("enter char")[0]
# print (ch)
# result = eval (input("Enter a expression - "))
# print (result)
# label .myLabel

counter = 0
lst = [10,20,30,"nishit",3.4,55]
for counter in lst:
    print (counter)

for counter in range(20,10,-1):
    print (counter)

alpha = 5

while alpha>=1:
    print ("Hello" , str(alpha), end=" ")
    alpha=alpha-1

print()

a,b = int(input("Enter value of a")),int(input("Enter value of b"))

if a==b:
    #a = a+b
    #b = a-b
    #a = a-b

    #a = a^b
    #b = a^b
    #a = a^b
    print('You have entered same values, please enter different values')
    #a, b = int(input("Enter value of a")), int(input("Enter value of b"))
    # goto .myLabel;
else:
    a,b = b,a
    print("new value of a is " + str(a))
    print("new value of b is "+ str(b))