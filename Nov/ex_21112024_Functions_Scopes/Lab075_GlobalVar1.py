# Global Variables
global_var_b = 10    # This is Global Variables any var which is on top

def my_fun():
    local_var_a = 5
    print(local_var_a)
    print(global_var_b)

print(global_var_b)
my_fun()