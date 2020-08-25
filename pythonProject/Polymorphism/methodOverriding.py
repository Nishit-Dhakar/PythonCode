
class A:
    def show(self):
        print("In Class A -Show Method")

class B(A):
    def show(self):
        print("In Class B -Show Method (Overridden)")


demo = B()
demo.show()