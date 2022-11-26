#Vehicle Class
class Vehicle:
    #class variables: not using
    #constructor in java or initialize an object's state(attribute) or
    #simple initializing object variables
    #It runs as soon as object is initiated
    def __init__(self,brand,model,type):
        self.brand = brand
        self.model = model
        self.type = type
        self.fuel_tank_size = 20
        self.fuel_level = 0
    #method or this reference in java (behaviour of object)
    #it always consist of self parameter
    #other parameters can also be included if needed
    def fueling(self):
        self.fuel_level = self.fuel_tank_size
        print('Fuel tank full')

    #another method or commonly known as behaviour of object
    def driving(self):
        print(f"{self.model} is driving now.")

    #method to increment an attribute’s value
    def update_fuel_level(self, new_level):
        if new_level <= self.fuel_tank_size:
            self.fuel_level = new_level
        else:
            print('Exceeded capacity')

    def get_gas(self, amount):
        if (self.fuel_level + amount <= self.fuel_tank_size):
            self.fuel_level += amount
            print('Added fuel.')
        else:
            print('The tank wont hold that much.')

#initiating objects
vehicle_1 = Vehicle('Maruti', '800', 'Car')
vehicle_2 = Vehicle('Scorpio', 'base', 'Car')

#Accessing object variables or attributes
print(vehicle_1.brand, vehicle_1.model, vehicle_1.type)
print(vehicle_2.brand, vehicle_2.model, vehicle_2.type)

#calling methods or behaviour of objects
vehicle_1.fueling()
vehicle_2.update_fuel_level(2)
vehicle_2.driving()
