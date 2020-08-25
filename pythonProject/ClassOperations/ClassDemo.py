
class MyFirstClass:
    #class variable
    machinetype = "computer"
    def __init__(self,cpu,ram):
        print("Inside __init__")
        self.cpu = cpu
        self.ramsize = ram

    def HelloFromClass(self):
        print("Nishit Dhakar is learning Class in Python")
        print("Nishit Laptop is {} with {} ram".format(self.cpu,self.ramsize))

    def compareClasses(self,other):
        if self.cpu == other.cpu:
            return True
        else:
            return False

a = MyFirstClass("i5","8Gb")
b = MyFirstClass("i7","16Gb")
MyFirstClass.machinetype = "ipad"

a.HelloFromClass()
if a.compareClasses(b) == True:
    print("both are same", a.machinetype, b.machinetype)
else:
    print("Both are different", a.machinetype, b.machinetype)

print(type(a))

#Alternate way to call method from a class
#MyFirstClass.HelloFromClass(a)