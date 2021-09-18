class Car():
    # __init__ is also called constructor method
    def __init__(self, modelname, year, price):
        self.modelname = modelname
        self.year = year
        self.price = price

    def price_inc(self):
        self.price = int(self.price*1.15)


honda = Car("City", 2017, 100000)
honda.cc = 1500

# if i want to see complete values of one object we will
# use namespace and for this will use __dict__
print("Honda Properties: ", honda.__dict__)
print(honda.price)
honda.price_inc()
print(honda.price)
