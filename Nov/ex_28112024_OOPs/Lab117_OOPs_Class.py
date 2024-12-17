class Person:
    # Attributes - What you have?

    id = None
    name = None
    age = None
    email = None
    height = None
    gender = None
    phone_no = None
    address = None

    # Behaviour - what you can do?

    def talk(slef):
        print("I can talk")

    def sleep(slef, name):
        print("I am a Method!!")
        print("Sleep", name)

    def sleep2(slef, name):  # Arg with return
        print("I am a Method!!")
        return None

    def walk(slef):
        print("I am walking")

    def walk_return(slef):  # NO Arg with return
        return "I am walking"

# Create an object of a class
# ObjectRef = ClassName() -> Object
geeta = Person()
geeta.name = "Geeta Sharma"
geeta.gender = "Female"


