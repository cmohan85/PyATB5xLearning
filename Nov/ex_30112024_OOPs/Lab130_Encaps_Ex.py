# Encapsulation
# Hide the data members (class variables, instance variables) by using only methods
class Car:
    def __init__(self):
        self.password = "kchenna" # public instance variable
        self.__password_secure = "pass123"  # private instance variable

    def chnange_password(self):
        print(self.password)

object_ref = Car()
print(object_ref.password)
print(object_ref.__password_secure)  # Car object has no attribute   __password_secure

