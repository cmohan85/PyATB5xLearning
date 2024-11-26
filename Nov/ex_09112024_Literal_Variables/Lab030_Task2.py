# Task
# Take2 input form user
# perform the Quotient and reminder
# 15 -> num1
# 2 -> num2
# Q -> 7
# R -> 1

num1 = float(input("Enter the first  number: "))
num2 = float(input("Enter the second  number: "))

q = num1 // num2
print(f'Quotient of given number is: -> {q}')
r = num1 % num2
print(f'Reminder of given number is: -> {r}')