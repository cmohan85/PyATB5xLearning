# *args
def print_mul_arguments(*args):
    # *args -> List
    for i in args:
        print(i)

print_mul_arguments("kchenna")
print_mul_arguments('Chenna', 'Krishna' , 'Mohan')
print_mul_arguments('kchenna', 10, True, False, "KrishnaMohan")