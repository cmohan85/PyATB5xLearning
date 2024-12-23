class A:

    def method(self):
        return "Method A"

class B:

    def method(self):
        return "Method B"

class C(B,A): # Multiple is FCFS
    pass

c = C()
print(c.method())