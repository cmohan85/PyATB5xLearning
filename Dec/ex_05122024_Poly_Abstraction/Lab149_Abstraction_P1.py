# Abstraction - Hide the details and show what is required
# Car -> multiple - Engine, GearBox
# Car -> driver -> Engine, gearbox ?

from abc import ABC, abstractmethod

class Animal(ABC):
    def __int__(self,name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):

    def make_sound(self):
        print("Bark Bark .......")

obj_dog = Dog()
obj_dog.make_sound()
