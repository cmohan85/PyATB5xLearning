# Problem to find the max between 3 numbers

num1 = float(input('Enter first number:'))
num2 = float(input('Enter Second number:'))
num3 = float(input('Enter third number:'))

if num1 > num2 and num1 > num3:
    print('Max no is: ', num1)
elif num2 > num1 and num2 > num3:
        print('Max no is: ', num2)
else:
    print('Max no is: ' , num3)
