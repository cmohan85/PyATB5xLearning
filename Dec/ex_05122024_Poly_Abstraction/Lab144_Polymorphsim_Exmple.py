# Method Overloading -> traditional method overload is not supported in python
# for this we have to use default values
class Calc:
    def sum(self,a,b):
        return a + b
    def sum(self,a,b,c):
        return a + b + c

calc_ref = Calc()
result = calc_ref.sum(3,4)
print(result)