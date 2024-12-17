class Dog:

    name = "chow"
    breed = None
    height = None

    def __init__(self):  # this is python constructor
        print("I will be called")

    def bark(self):
        print("Barking")

    def sleep(self):
        print("Sleep")

# Object Ref
chow = Dog()
# Dog() -> is Object
# chow -> is Object Ref.
mow_ref = Dog()
bow_ref = Dog()

print(mow_ref.name)
print(bow_ref.name)

