# Dictionary from two Lists

keys = ["name" , "role", "exp"]
values = ["kchenna", "OCI", 7]

my_dict = dict(zip(keys,values))
print(my_dict)

# Merge two Dictionarys
dict1 = {"a":1, "b":2}
dict2 = {"c":3, "d":4}
merge_dict = dict1 | dict2
print(merge_dict)
print(merge_dict.get("a"))

