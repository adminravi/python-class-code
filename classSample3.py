#using class variables
class Cat:
    #class variable
    species = 'animal'
    #constructor in java
    def __init__(self,breed,color):
        #instance variable
        self.breed = breed
        self.color = color

stacy = Cat('Balinese', 'Black')
pomp = Cat('Chinchilla', 'White')

print("Stacy details: ")
print("Stacy is an", stacy.species)
print("Stacy's breed is", stacy.breed)
print("Stacy's color is", stacy.color)

print("pomp details: ")
print("pomp is an", pomp.species)
print("pomp's breed is", pomp.breed)
print("pomp's color is", pomp.color)
