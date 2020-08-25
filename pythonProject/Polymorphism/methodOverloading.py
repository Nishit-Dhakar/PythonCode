
class marks:
    def __init__(self,science,math):
        self.science = science
        self.math = math
        print("Science marks {}, Math Marks {}".format(science,math))

    # def sum(self,str,a=None,b=None):
    #     print("Sum simple {}".format(str))
    #     return a+b;

    def sum(self,a=None,*b):
        sum=a
        for i in b:
            sum+=i
        return sum;

std2 = marks(80,91)
print(std2.sum())
print(std2.sum(200,21,22))

