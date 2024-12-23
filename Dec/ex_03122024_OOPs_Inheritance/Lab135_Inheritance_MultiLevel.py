# Multilevel Inheritance

class GrandFather:
    gold = "2kg"

    def BHK1(self):
        print("1BHK")

class Father(GrandFather):
    diamond = "22 karat"

    def BHK2(self):
        print("2BHK")

class Son(Father):
    btc = "1 BTC"

    def BHK3(self):
        print("3BHK")

son = Son()
print(son.gold)
print(son.diamond)
print(son.btc)
print("-----------")

father = Father()
print(father.gold)
print(father.diamond)
print("-----------")

grand = GrandFather()
print(grand.gold)