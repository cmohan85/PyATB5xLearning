# Static Methods
# A static method is a method that belongs to a class rather than an
# instance of the class.

class O:
    @staticmethod
    def sum(a,b):  # static method
        return a + b

    def sub(self,a,b): # normal method
        return a - b

O_obj = O()
result = O_obj.sub(1,2)
print(result)
print("----------")
print(O.sum(2,3))