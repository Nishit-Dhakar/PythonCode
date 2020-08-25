#Multiple Inheritnce example

"""
This is a parent class for Practicing the inheritnce
Also its a test of how documentation comments works :)
"""
class parent:
    def __init__(self):
        print("In Constructor of Parent")
    @classmethod
    def feature1(self):
        print("We are in Feature 1 of Parent")

    def feature2(self):
        print("We are in Feature 2 of Parent")

class child():
    #If child constructor is not explictly defined, then
    # object of child class will go to parent class constructor
    def __init__(self):
        #we can explicitly call init of parent by using super()
        #super().__init__()
        print("In Constructor of child")
    @staticmethod
    def feature3(self):
        print("We are in Feature 3 of child")

    def feature2(self):
        print("We are in Feature 2 of Child")

class grandchild(parent,child):
    def __init__(self):
        #Super() init call be take the first class from which this
        #class is inheriting. Left most calls and call the
        #constructor of the same.
        super().__init__()
        print("In constructor of grand child")

demo = grandchild()
demo.feature1()
demo.feature3(demo)
demo.feature2()
