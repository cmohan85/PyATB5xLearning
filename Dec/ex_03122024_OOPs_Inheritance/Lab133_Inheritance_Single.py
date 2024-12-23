# Single Inheritance -> 85% of the time you will use Single  Inherit. in API, web automation

class Father:
    key = "2BHK"

    def car(self):
        print("Father has a Car -> Alto")
        print(self.key)

class Son(Father):  # Single inheritance
    key2 = "3 BHK"

    def suv(self):
        print("Nissan Magnite, Black")
        print(self.key2)

father_object = Father()
father_object.car()

son_object = Son()
son_object.suv()

son_object.car()