class Parrot:
    #class attribute
    species = 'bird'
    #instance attribute
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
#instantiating the Parrot class
pet_1 = Parrot('Pihu', 10)
pet_2 = Parrot('Jihu', 9)
#accessing class attribute
print(f"Pet 1 is a {pet_1.__class__.species}")
print(f"Pet 2 is also a {pet_2.__class__.species}")

#accessing instance attribute
print(f"{pet_1.name} age {pet_1.age} years loves to sing")
print(f"{pet_2.name} age {pet_2.age} years loves to dance")
    

