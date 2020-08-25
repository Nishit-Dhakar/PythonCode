#Multiple Inheritnce example
class parent:
    def feature1(self):
        print("We are in Feature 1 of Parent")

    def feature2(self):
        print("We are in Feature 2 of Parent")

class child(parent):
    def feature3(self):
        print("We are in Feature 3 of child")

    def feature4(self):
        print("We are in Feature 4 of child")

class grandchild(child):
    def feature5(self):
        print("We are in Feature 5 of grand child")

# demo = grandchild()
# demo.feature1()
# demo.feature2()
# demo.feature3()
# demo.feature4()
# demo.feature5()

#Inheritence from multiple objects
class uncle:
    def feature1(self):
        print("We are in Feature 1 of Uncle")


class Mama:
    def feature3(self):
        print("We are in Feature 3 of Mama")

class kid(uncle,Mama):
    def feature5(self):
        print("We are in Feature 5 of kid")

demo = kid()
demo.feature1()
demo.feature3()
demo.feature5()