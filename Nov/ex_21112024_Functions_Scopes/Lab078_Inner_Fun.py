# Outer functions - var can be used by the inner functions.
def outer_fun():
    var1 = 10 # local

    def inner_fun():
        print(var1)

    def inner_fun2():
        print(var1)

    inner_fun()
    inner_fun2()

outer_fun()