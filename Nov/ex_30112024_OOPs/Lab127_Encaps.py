# Encapsulation
class Car:

    def __init__(self,o_name,o_make,o_model):
        self.name = o_name
        self.make = o_make
        self.model = o_model

    def start_engine(self):
        print("Starting a car with the name " + self.name)
        print("Starting a car with the make " + self.make)
        print("Starting a car with the model " + self.model)

lambo = Car("Lambo", "V6", "2023")
lambo.start_engine()

print("------------------------")

Nissan = Car("Nissan", "1L Turbo", "2022")
Nissan.start_engine()