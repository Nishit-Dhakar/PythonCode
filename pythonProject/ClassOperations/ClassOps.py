class student:
    schoolname = "JPIS"
    def __init__(self,eng,mat,sci):
        self.eng = eng
        self.mat = mat
        self.sci = sci

    def average(self):
        return (self.mat+self.sci+self.eng)/3

    #Getter Method of class - similar to get of properties
    #THese are also called as accessors as they get values
    def get_eng(self):
        return self.eng
    #setter method of class is similar to set of properties
    #these are also called as mutators as they modify values
    def set_eng(self,newval):
        self.eng = newval;

    #method to access class variable - key word is cls
    @classmethod
    def schoolInfo(cls):
        return cls.schoolname

    #static method
    @staticmethod
    def info():
        return("This is a static method")

aryaa = student(97,98,99)
print(aryaa.average())
print(student.info())
print(student.schoolInfo())

