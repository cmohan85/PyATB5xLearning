# Decorators
def add_secutiry(func):

    def wrapper():
        print('1. Before the function is called')
        print('2. Add Helmet, Dashcash, gloves, knee guards, License')
        func()
        print('3. After the function is called')
        print('4. Secure driving, Leave all the items')

    return wrapper()

@add_secutiry
def driving_scooty():
    print("Normal Functiona!")
    print('I am Driving Scooty')