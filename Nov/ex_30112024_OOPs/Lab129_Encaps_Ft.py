# Web Automation - we will use Selenium
# Page - You are going to automate

class VWOLoginPage:
    def __init__(self, email_arg, password_arg):
        self.email = email_arg
        self.password = password_arg

    def login_confirm(self):
        if self.email == "abcd@gmail.com" and self.password == "Pass123":
            print("Allowed, Login Success")
        else:
            print("Login Failed")

# email = input("Enter the mailid\n")
# password = input("Enter thepasword\n")
#
# email = # Read from test data - Excel,CSV or Env file
# password = # Read from test data - Excel,CSV or Env file

# vwo_obj = VWOLoginPage(email,password)
# vwo_obj.login_confirm()

kchenna = VWOLoginPage("abcd@gmail.com", "Pass123")
kchenna.login_confirm()