# w.a.p that prints number from 1 to 100
# However, for multiples of 3, print "Fizz" instead of the numbers,
# and for multiple of 5, print "Buzz" for numbers that are
# multiple of both 3 and 5, print "FizzBuzz" (for, if)

for numbers in range (1,101):
    if numbers % 3 == 0 and numbers % 5 == 0:
        print("FizzBuzz")
    elif numbers % 5 == 0:
        print('Buzz')
    elif numbers % 3 == 0:
        print('Fizz')
    else:
        print(numbers)