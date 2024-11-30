# Problem to find the max btwn two numbers

num1 = float(input('Enter first number:'))
num2 = float(input('Enter Second number:'))

if num1 >= num2:
    print("Max no is :", num1)
else:
    print("Max no is :", num2)

# Edge case her is num1 == num2 -> how to handle
# String -> ABC, ten. then we have to use try and except - we will learn in future
# -ve value  -> we will learn in future