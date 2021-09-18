class Parent:
    def __init__(self, fname, fage):
        self.name = fname
        self.age = fage

    def view(self):
        print(self.name, self.age)


class Child(Parent):
    def __init__(self, fname, fage):
        Parent.__init__(self, fname, fage)
        self.lastname = "Shabbir"

    def view(self):
        print(self.name, self.lastname, self.age)


ob = Child("Faiqa", 19)
ob.view()


