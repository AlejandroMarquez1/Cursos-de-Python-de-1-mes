# Abstracts class
# Abstracts class = A class that cannot be instantiated on its own; Meant to be subclassed/
# They can contain methods, which are declared but no implementation/
# Abstracts classes benefits:
# 1. Prevents instantiation of the class itself
# 2. Requires children to use inherited abstracts methods

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("You drive the car")
    def stop(self):
        print("You stop the car")

car1 = Car()
car1.go()
car1.stop()


class Motorcycle(Vehicle):
    def go(self):
        print("You ride the motorcycle")
    def stop(self):
        print("You stop the motorcycle")

motorcycle = Motorcycle()
motorcycle.go()
motorcycle.stop()

class Boat(Vehicle):
    def go(self):
        print("You sail the boat")
    def stop(self):
        print("You anchor the boat")

boat = Boat()
boat.go()
boat.stop()