class arithamaticOps:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print(a+b)

    def add(self, a, b):
        print(a + b)

class displaymsg:
    def add(self,a,b):
        print("Hello, i just display message and do nothing :)")

class helpme:
    def add(self,ops):
        ops.add(5,10)

art =arithamaticOps(10,20)
newl = displaymsg()

demo = helpme()
demo.add(art)
demo.add(newl)
