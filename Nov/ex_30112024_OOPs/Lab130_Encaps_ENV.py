# Web Automation - we will use Selenium
# Page - You are going to automate

from dotenv import load_dotenv
import os

class VWOLoginPage:
    def __init__(self, email_arg, password_arg):
        self.email = email_arg
        self.password = password_arg

    def login_confirm(self):
        if self.email == "abcd@gmail.com" and self.password == "Pass123":
            print("Allowed, Login Success")
        else:
            print("Login Failed")

load_dotenv()
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

vwo_obj = VWOLoginPage(email,password)
vwo_obj.login_confirm()
