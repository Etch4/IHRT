def addtu(func):
    def inner(self):
        return f"{func(self)} \U0001F44D"
    return inner

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    @addtu
    def printname(self):
        return f"{self.fname} {self.lname}"

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

x = Student("tito", "The_IceBreaker")
print(x.printname())
