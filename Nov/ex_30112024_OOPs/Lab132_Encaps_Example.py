
class Home:
    def __init__(self):
        self.public_var = "father"
        self.__private_var = "child"

    def mom(self):
        print(self.__private_var)

object_ref = Home()
object_ref.mom()
print(object_ref.public_var)
# print(object_ref.__private_var) # AttributeError: 'Home' object has no attribute '__private_var'