from Nov.ex_28112024_OOPs.Lab122_Calc import object_ref


class Calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

object_ref1 = Calc(3, 4)
object_ref2 = Calc(3, 4)
object_ref3 = Calc(3, 4)
object_ref4 = Calc(3, 4)

output = object_ref1.sum()
print(output)
