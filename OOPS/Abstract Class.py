# Abstract class to hide information as their don't affect the
# functionality

from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def price(self, x):
        pass


bj = Car("Honda City")
