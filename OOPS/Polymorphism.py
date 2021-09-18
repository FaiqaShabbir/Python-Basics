"""
When the function is called using the object audi then the
function of class Audi is called and when it is called using
the object bmw then the function of class BMW is called.
"""


class Audi:
    def description(self):
        print("This description is for AUDI!")


class BMW:
    def description(self):
        print("This description is for BMW!")


audi = Audi()
bmw = BMW()
for car in (audi, bmw):
    car.description()