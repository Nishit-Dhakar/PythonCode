
class marks:
    def __init__(self,science,math):
        self.science = science
        self.math = math
        print("Science marks {}, Math Marks {}".format(science,math))

    #Example of operator overloading
    def __add__(self, other):
        science = self.science + other.science
        math = self.math + other.math
        newstd = marks(science,math)
        return newstd

    #Overloading of greater than method
    def __gt__(self, other):
        if(self.math > other.math):
            return True
        else:
            return False
    #This is similar str which is used to print(a)
    def __str__(self):
        return '{} {}'.format(self.math, self.science)

std1 = marks(94,97)
std2 = marks(80,91)
std3 = std1 + std2
print(std1 > std2)
print(std1)
#sum = a + b
#if we call a+b then in background int.__add__(a,b))
#is getting called
#print(a+b)
