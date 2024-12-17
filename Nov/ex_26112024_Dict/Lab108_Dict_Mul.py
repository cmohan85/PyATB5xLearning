student_info1 = {
    "name" : "kchenna",
    "age" : 32,
    "address" : {
        "home_address" : "TG",
        "Office_address" : "KA"
    }
}

student_info2 = {
    "name" : "Mohan",
    "age" : 30,
    "address" : {
        "home_address" : "GOA",
        "Office_address" : "KA"
    }
}

student_list = [student_info1, student_info2]
print(student_list)
print(student_list[0])
print(student_list[0]["name"])
print(student_list[0]["age"])
print(student_list[0]["address"]["home_address"])

print(student_list[1])