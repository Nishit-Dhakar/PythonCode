
def div(a,b):
    if(a<b):
        a,b = b,a
    return a/b;

#Using Decorator to modify function behaviour

def divide(a,b):
    print(a/b)

#create a function which takes function as parameter
def smart_div(func):
    #define a function inside the function which
    # takes same variables as original funciton
    def newDiv(a,b):
        #Make changes what we need
        if (a < b):
            a, b = b, a
        #return function with new updated variables
        return func(a,b)
    #return function
    return newDiv

divide = smart_div(divide)
res = divide(10,20)
