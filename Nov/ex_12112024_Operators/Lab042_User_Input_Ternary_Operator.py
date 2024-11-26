# w a p - if age is > 18 allow to vote
# else -> not allowed to vote


#user_age = int(input("Enter your age:  \n"))

# if user_age > 18:
#     print("Your are allowed to Vote")
# else:
#     print("You are not allowed to Vote")

print("Your are allowed to Vote" if int(input("Enter your age:  \n")) > 18 else "You are not allowed to Vote")