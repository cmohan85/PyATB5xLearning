# Match Statement is similar to Switch statement in java
# Match is applicable if python > 3.10

#  w.a.p to ask the user which browser he wants to run automation

browser_name = input("Enter the browser name\n")
match browser_name:
    case "firfox":
        print("Starting Firefox!!!")
    case "chrome":
        print("Starting chrome!!!")
    case "edge":
        print("Starting edge!!!")
    case "safari":
        print("Starting safari!!!")
    case _: # default
        print("No browser found!")
