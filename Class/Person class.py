class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def greet(abc):
        print("Hello name is", abc.name)


p1 = Person("John", 30)
p1.greet()
p1.age = 40
del p1.age
print(p1.age)
