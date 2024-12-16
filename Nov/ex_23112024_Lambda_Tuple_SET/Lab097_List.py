from Nov.ex_23112024_Lambda_Tuple_SET.Lab096_List import my_list2

my_list = [1, 2, 3]

# Indexing
print('Element at the index 0 - ', my_list[0])
print('Element at the index 1 - ', my_list[1])
print('Element at the index 2 - ', my_list[2])

# append() - # Append object to the end of the list.
my_list.append(4)
my_list.append(5)
print(my_list)

# extend() - # Append a new list
my_list.extend([6,7,8])  # extend takes list thus why [6,7,8]
print(my_list)

# insert()
my_list.insert(1,'kchenna')
print(my_list)
print(len(my_list))


my_list.insert(0,0)
print(my_list)

my_list[1] = 'MOhan'
print(my_list)

# remove

my_list.remove('MOhan')
print(my_list)

print("--------------------")

my_copy_list = my_list.copy()
print(my_list)
print(my_copy_list)

my_list.remove("kchenna")
my_copy_list.remove("kchenna")

my_list.sort()
my_copy_list.sort()
print(my_list)
print(my_copy_list)