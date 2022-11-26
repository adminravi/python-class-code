class Namegame:
    #class variable
    classvariable = 'human'
    #constructor in java
    def __init__(self, first, last):
        self.first = first
        self.last = last
    #method or behaviour of objects
    def fullname(self):
        print(f"I am a {self.classvariable} and my fullname is: {self.first} {self.last}")
#instantiating objects (objects of class Namegame)
p1 = Namegame('Ravi', 'Verma')
p2 = Namegame('Vinci', 'Verma')
p3 = Namegame('Sri', 'Verma')


p1.fullname()


