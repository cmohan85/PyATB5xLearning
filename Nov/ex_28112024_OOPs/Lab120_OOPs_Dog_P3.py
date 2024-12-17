class Dog:

    name = None
    breed = None
    height = None

    def __init__(self, name, breed):  # this is python Parameterized constructor
        print("PC")
        self.name = name
        self.breed = breed


    def bark(self):
        print("Barking")

    def sleep(self):
        print("Who is Sleeping -> " + self.name)

# Object Ref

# Dog() -> is Object
# chow -> is Object Ref.
chow_ref = Dog("chow", "mastiff")
print(chow_ref.name)
chow_ref.sleep()
print(id(chow_ref))

mow_ref = Dog("mow" , "husky")
print(mow_ref.name)
mow_ref.sleep()
print(id(mow_ref))