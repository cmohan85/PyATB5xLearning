# Create a program to sum of three numbers from the user input
#if user doesn't enter any number, use default as 100, 200, 300
from Nov.ex_19112024_Functions.Lab069_Functions_Types2 import result

num1 = int(input("Enter the num1\n"))
num2 = int(input("Enter the num2\n"))
num3 = int(input("Enter the num3\n"))


def sum_of_three(n1=100, n2=200, n3=300):
    return n1 + n2+ n3

result1 = sum_of_three(num1,num2,num3)
print('Sum of three numbers is :', result1)


result2 = sum_of_three()
print('Sum of three numbers is :', result2)
