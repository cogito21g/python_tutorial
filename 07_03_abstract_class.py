# class
## abstract class

from abc import *

class Person(metaclass=ABCMeta):
    @abstractmethod
    def say(self):
        pass

class Asian(Person):
    type = 'Asian'
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __del__(self):
        print(f"{self.name} destroyed")

    def say(self):
        print(f"Hello my name is {self.name}")

lee = Asian("lee", 20)
lee.say()
