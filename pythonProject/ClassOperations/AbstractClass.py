from abc import ABC,abstractmethod

class machine(ABC):
    @abstractmethod
    def process(self):
       pass

class laptop(machine):
    def process(self):
        print("Processing...")


a = laptop()
a.process()