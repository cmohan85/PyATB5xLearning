my_dic = {
    "name" : "kchenna",
    "age" : 32,
    "role" : "OCI",
    "experience" : 7
}
print(my_dic)
print(my_dic["age"])

my_dic["role"] = "SDET"
print(my_dic)

del my_dic["age"]
print(my_dic)

for key,value in my_dic.items():
    print(key," --> ", value)

print("age" in my_dic)
print("name" in my_dic)

