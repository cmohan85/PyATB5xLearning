
def sum_three(a=1,b=1,c=1):
    return a + b + c

result1 = sum_three()
print(result1)

result2 = sum_three(1,2)
print(result2)

result3 = sum_three(1,2,3)
print(result3)

result4 = sum_three(b=10, a= 11, c=13)
print(result4)