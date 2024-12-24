class Parent:
    def home(self):
        print("2BHK")


class Son(Parent):
    def home(self):
        print("3BHK")

ob_ref = Son()
ob_ref.home()