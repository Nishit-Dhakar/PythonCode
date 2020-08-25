

class student:
    schoolname = "JPIS"
    def __init__(self,name,percentage):
        self.name = name
        self.percentage = percentage
        #object of inner class in constructor of outer class
        self.personal = self.personaldetails(12,"Indian")

    def show(self):
        print(self.name , " ", self.percentage, end=" ")

    #method to access class variable - key word is cls
    @classmethod
    def schoolInfo(cls):
        return cls.schoolname

    #static method
    @staticmethod
    def info():
        return("This is a static method")

    class personaldetails:
        def __init__(self,age,citizenship):
            self.age = age
            self.citizenship = citizenship

        def show(self):
            print(self.age, " ", self.citizenship)

aryaa = student("Aryaa",97)
aryaa.show()
aryaa.personal.show()

personaldata = aryaa.personal
personaldata.show()
#print(student.info())
#print(student.schoolInfo())
