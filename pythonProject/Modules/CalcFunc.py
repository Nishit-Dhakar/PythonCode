
result =0;
if __name__ == "__main__":
    print("CalcFunc module: "+__name__)

#Method to perform addition of 2 or more numbers
def Add(a,*b):
    global result
    result = a
    for i in b:
        result = result +i;
    return result;

#Method to perform substraction of 2 or more numbers
def Substract(a,*b):
    global result
    result = a
    for i in b:
        result = result - i;
    return result;

#Method to perform Division of 2 numbers
def Divide(a,b):
    if a < b:
        a, b = b, a
    return a/b;

#Method to perform addition of 2 or more numbers
def Multiply(a,*b):
    global result
    result = a
    for i in b:
        result = result * i;
    return result;