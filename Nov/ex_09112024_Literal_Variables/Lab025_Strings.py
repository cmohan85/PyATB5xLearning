name = "This is a Big line"
print(type(name))

#name = name + 1  #TypeError: can only concatenate str (not "int") to str
name = name + str(1)

print(name)

first_name = 'Krishna'
last_name = 'Mohan'
full_name = first_name + " " + last_name
print(full_name)
print(type(full_name))