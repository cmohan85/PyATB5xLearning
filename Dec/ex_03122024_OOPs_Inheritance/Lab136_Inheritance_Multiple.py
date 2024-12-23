# Multiple Inheritance

class Father:

    def home(self):
        print("This is father home")

    def father_money(self):
        return 5

class Mother:

    def home(self):
        print("This is mother home")

    def mother_money(self):
        return 2

#class Son(Mother, Father): # Multiple inher. will give First Serv Fist Come, if same method name

class Son(Father, Mother):
    def print_info(self):
        print("son")

s = Son()
print(s.father_money())
print(s.mother_money())
print(s.home())