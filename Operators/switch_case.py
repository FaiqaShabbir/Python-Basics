# through dictionary and method
def week(i):
    switcher = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }
    return switcher.get(i, "Invalid input")


print(week(6))


# Using Python Functions & Lambdas

def zero():
    return 'zero'


def one():
    return 'one'


def indirect(i):
    switcher = {
        0: zero,
        1: one,
        2: lambda: 'two'
    }
    func = switcher.get(i, lambda: 'invalid input')
    return func()


print(indirect(0))


# With Python Classes

class Switcher(object):
    def indirect(self, i):
        method_name = 'number_' + str(i)
        method = getattr(self, method_name, lambda: 'invalid input')
        return method()

    def number_0(self):
        return 'zero'

    def number_1(self):
        return 'one'

    def number_2(self):
        return 'two'


s = Switcher()
print(s.indirect(2))
