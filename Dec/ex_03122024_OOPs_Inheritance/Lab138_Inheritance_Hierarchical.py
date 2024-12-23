# Hierarchical Inheritance
class Father:

    def BHK1(self):
        print("1BHK")

class Krishna(Father):

    def BHK2(self):
        print("2BHK")


class Mohan(Father):

    def BHK3(self):
        print("3BHK")


class Kchenna(Father):

    def no_house(self):
        print("No House")

krishna = Krishna()
krishna.BHK1()
krishna.BHK2()

mohan = Mohan()
mohan.BHK1()
mohan.BHK3()
#mohan.BHK2()  -> NO , it belongs to Krishna

kchenna = Kchenna()
kchenna.BHK1()
#kchenna.BHK2() -> NO , it belongs to Krishna
#kchenna.BHK3() -> NO , it belongs to Mohan
kchenna.no_house()
