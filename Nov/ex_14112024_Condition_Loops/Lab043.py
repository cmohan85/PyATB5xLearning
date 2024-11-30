# w.a.p to take a user age and
# let him know if he can go the club.
# 21

age = int(input('Enter your are \n'))

if age > 21:
    print("You are allowed to club")
else:
    print('your are not allowed to club')

# check for the edge case.
# we should consider edge cases such as:
# Nagative or extem values will breake the program
# Non-numberic input like ABC
# Age which is valid -> 130