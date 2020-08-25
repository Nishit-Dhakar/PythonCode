a = 10
b=20

#function start
def printerfun():
    global a
    a=17
    print(a)
    globals()["b"] = 15
    print(b)
#function end

printerfun();
print(a)
print(b)