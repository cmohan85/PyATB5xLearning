class Calc:
    def sum(self,a=0,b=0):
        return a + b
    def sum(self,a=0,b=0,c=0):
        return a + b + c

calc_ref = Calc()
result = calc_ref.sum(3,4)
print(result)