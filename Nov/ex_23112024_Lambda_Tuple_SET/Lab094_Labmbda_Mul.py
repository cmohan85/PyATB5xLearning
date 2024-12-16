# w.a.p to calculate even and odd

def find_even_odd(num):
    if num % 2 == 0:
        print('Even')
    else:
        print("Odd")

find_even_odd(5)
find_even_odd(540)

# with lambda
check_even_odd = lambda num: "Even" if num % 2 == 0 else "Odd"
print(check_even_odd(5))
print(check_even_odd(540))