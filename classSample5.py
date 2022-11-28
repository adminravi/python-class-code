class Person:
    def __init__(self,first,last):
        self.first = first
        self.last = last

    def fullname(self):
        return f"Fullname is: {self.first} {self.last}"

x1 = Person("Ravi", "Verma")
x2 = Person("Latika", "Sharma")

print(x1.fullname())
print(x2.fullname())

class Student(Person):
    def __init__(self,first, last, year):
        #Person.__init__(self,first,last)
        super().__init__(first,last)
        self.graduationyear = year
    def welcome(self):
        print(f"Welcome {self.first} {self.last} to the class of {self.graduationyear}")

x3 = Student("Aadyant", "Verma", 2022)
x4 = Student("Aakarshit", "Verma", 2019)
print(x3.fullname())
x3.welcome()
print(x4.fullname())
x4.welcome()
