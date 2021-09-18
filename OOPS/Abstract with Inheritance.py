from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, name):
        self.name = name

    def description(self):
        print("This the description function of class car.")

    @abstractmethod
    def price(self, x):
        pass


class new(Car):
    def price(self, x):
        print(f"The {self.name}'s price is {x} lac")


obj = new("Honda City")

obj.description()
obj.price(25)


"""
Car is the abstract class that inherits from the ABC class 
from the abc module. 
"""