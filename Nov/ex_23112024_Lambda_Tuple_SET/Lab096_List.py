# List -  Collection of items
# grocery List - butter, bread, banana, panner
# 10th marks - 91,92,90,78,56

my_list = [1, 2, 3] # Same type of data (int)
my_list2 = [1, True, "Kchenna", 12.34]

print(my_list)
print(len(my_list))
print(my_list[0])
print(my_list[1])
print(my_list[2])
# print(my_list[3]) # IndexError: list index out of range
# print(my_list[4]) # IndexError: list index out of range

my_list[0] = 'chenna'
my_list[1] = 'krishna'
my_list[2] = 'mohan'
print(my_list)

print('----')

for item in my_list2:
    print(item)