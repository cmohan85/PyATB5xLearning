# User Defined
# 1. They can't return -> non return
# 2. They can return something
# 3. They have parameters
# 4. They don't have parameters / arguments

# 1. They can't return -> non return
# No return type and no parameter / argument - NRNP

def greet():
    print('Hi')

greet()


# 2. They can return type with argument

def greet_user(input_name):
    print("Hello ,Mr. " , input_name)

greet_user("Mohan")


# 3. No return type  and with default argument ( or positional arguments)

def say_hello_default_arg(name="Mohan"):
    print("Hello" , name.upper())

say_hello_default_arg("kchenna")
say_hello_default_arg()


# multiple arguments
def multiple_args(name1='A',name2='B'):
    print('Mul -> ', name1, name2)

multiple_args()
multiple_args(name1='kchenna')
multiple_args(name1='krishna', name2='Mohan')



# 4. Argument + Return type

def sum_of_two(a,b):
    return a + b

result = sum_of_two(6,54)
print(result)