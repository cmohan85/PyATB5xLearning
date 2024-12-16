import math

# def give_me_power(num):
#     return math.pow(num, 2)
#
# result = give_me_power(10)
# print(result)

# Lambda code

result = lambda : math.pow(int(input('Enter the num\n')),2)
print(result())  # Lambda always return a function, we call a function