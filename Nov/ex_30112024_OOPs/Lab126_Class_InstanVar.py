class Person:

    def __init__(self,name):
        self.name = name

    def walk(self):
        return self.name

Krishna = Person("krishna")
Mohan = Person("mohan")
print(Krishna.name)
print(Mohan.name)

print("Who is walking -> ", Krishna.walk())
print("Who is walking -> ", Mohan.walk())

