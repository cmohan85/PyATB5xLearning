# Polymorphsim - two types
# Method overloading and Method overriding (but python doesn't support method overriding)
# Now example of Method Overloading

class Dog:
    def bark(self):
        print("Dog is Barking")

    def bark(self,breed):
        print(f"Dog with {breed} is barking")

d = Dog()
#d.bark()
d.bark("chow")