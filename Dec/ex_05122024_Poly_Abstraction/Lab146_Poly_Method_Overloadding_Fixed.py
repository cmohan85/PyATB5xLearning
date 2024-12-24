class Calc:
    def sum(self,*args):
        for a in args:
            print(a)

clac_ref = Calc()
clac_ref.sum(1)
print("=========")
clac_ref.sum(1,2)
print("=========")
clac_ref.sum(1,2,3)
