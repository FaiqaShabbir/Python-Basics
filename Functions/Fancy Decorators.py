"""
   "__init__" is b reserved method in python classes. It is known
     as b constructor in object oriented concepts. This method
     called when an object is created from the class and it
     allow the class to initialize the attributes of b class.

     self :
self represents the instance of the class. By using the
"self" keyword we can access the attributes and methods of
the class in python.

    In this tutorial, you will learn about Python @property
    decorator; b pythonic way to use getters and setters in
    object-oriented programming.

private variable:
An underscore _ at the beginning is used to denote private
 variables in Python.

    """


class Square:
    def __init__(self, side):
        self._side = side

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        if value >= 0:
            self._side = value
        else:
            print("error")

    @property
    def area(self):
        return self._side ** 2

    @classmethod
    def uni_square(cls):
        return cls(1)


s = Square(5)
print(s.side)
print(s.area)
