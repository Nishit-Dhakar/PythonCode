from threading import *
from time import sleep

class hello(Thread):
    #run is method of thread class
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

class hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)

a = hello()
b = hi()
(a.start())
sleep(.2)
(b.start())

#ask threads to wait for threads to finish before printing bye
a.join()
b.join()
print("bye")