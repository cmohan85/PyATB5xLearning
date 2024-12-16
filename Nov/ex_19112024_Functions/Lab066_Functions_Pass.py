def first_name_last_name():
    pass # in future i will complete this functions


def greet_to_all_of_you():
    print("Hello, All")


def greet():  # function in a function
    print("Hi,")
    greet_to_all_of_you()

greet()
greet_to_all_of_you()