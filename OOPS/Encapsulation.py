# Encapsulation = Private members of class

class Car:
    def __init__(self, name, mileage):
        self.__name = name
        self.mileage = mileage

    def description(self):
        return f"The {self.__name} car gives mileage of {self.mileage}km/l"


obj = Car("BMW 7-series", 39.53)

# accessing protected variable via class method
print(obj.description())

# accessing protected variable directly from outside
# print(obj.__name)
print(obj.mileage)
# Name Mangling
print(obj._Car__name)
