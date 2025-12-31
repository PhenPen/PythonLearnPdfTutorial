""" Object Oriented Programming"""

# So for OOP , We have 4 main pillars
# 1. Encapsulation : Bundling data and methods that operate on that data within one unit, e.g., a class.
# 2. Abstraction : Hiding complex implementation details and showing only the necessary parts.
# 3. Inheritance : A mechanism where a new class inherits properties and behavior (methods) from an existing class.
# 4. Polymorphism : The ability of different classes to be treated as instances of the same class through a common interface. It allows methods to do different things based on the object it is acting upon, even if they share the same name.

''' Polymorphism is when the same action means different things depending on who does it.

Think of it like this:

Imagine you tell three animals to "make a sound":

A dog makes a "Woof!"
A cat makes a "Meow!"
A duck makes a "Quack!"
You used the same command ("make a sound"), but each animal responded differently. That's polymorphism!'''


# Let's see each of them with examples

# 1. Encapsulation
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.__speed = 0  # Private attribute or Hidden attribute of a class becuase it is not passed as a parameter or accessed outside the class

    def accelerate(self, increment):
        self.__speed += increment
        print(f"The car has accelerated to {self.__speed} km/h")

    def brake(self, decrement):
        self.__speed -= decrement
        if self.__speed < 0:
            self.__speed = 0
        print(f"The car has slowed down to {self.__speed} km/h")

    def get_speed(self):
        return self.__speed
# Example usage
my_car = Car("Toyota", "Corolla", 2020)
my_car.accelerate(50)
my_car.brake(20)
print(f"Current speed: {my_car.get_speed()} km/h")

# 2. Abstraction
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self) -> str:
        pass

class Dog(Animal):
    def make_sound(self) -> str:
        return "Woof!"
class Cat(Animal):
    def make_sound(self) -> str:
        return "Meow!"

class Duck(Animal):
    def make_sound(self) -> str:
        return "Quack!"
    
# Example usage
animals = [Dog(), Cat(), Duck()]
for animal in animals:
    print(animal.make_sound())

# 3. Inheritance
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        print("Engine started")
class Motorcycle(Vehicle):
    def do_wheelie(self):
        print("Doing a wheelie!")
# Example usage
my_bike = Motorcycle("Harley-Davidson", "Street 750")
my_bike.start_engine()
my_bike.do_wheelie()

# 4. Polymorphism
class Bird:
    def fly(self):
        print("Flying in the sky!")
class Airplane:
    def fly(self):
        print("Flying through the clouds!")
# Example usage
def let_it_fly(flying_object):
    flying_object.fly()
sparrow = Bird()
boeing = Airplane()
let_it_fly(sparrow)
let_it_fly(boeing)

