# inheriting attributes of parent class in child class

class Car:
    def __init__(self, name, mileage):
        self.name = name
        self.mileage = mileage

    def description(self):
        return f"The {self.name} car gives mileage of {self.mileage}km/l"


class BMW(Car):
    pass


class Audi(Car):
    @staticmethod
    def audi_desc():
        return "This is the description method of class audi"


obj1 = BMW("BMW 7-series", 39.35)
print(obj1.description())

obj2 = Audi("Audi A8 L", 14)
print(obj2.description())
print(obj2.audi_desc())
