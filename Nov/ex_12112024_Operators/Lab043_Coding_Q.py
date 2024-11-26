# Write a python program to calculate the
# area of a circle given its radius using the formula
#  '''area=pi*r*r''' (take pie as 3.14)



radius = float(input('Enter the radius of the circle:'))
print(radius)
#area = float(3.14* pow (radius,2))
area = float(3.1434567* (radius**2))
print('Area of circle is: ' , area)
print(f'Area of circle is: -> : {area:.2f}')  # for two digit decimal

# * -> mul
# ** -> power

import math
print(math.pi)
print(math.pow(radius,2))
area = math.pi * math.pow(radius,2)
print('Area of circle is: ' , area)

print(math.pi)
print(math.pow(1,2))
print(math.sin(90))
print(math.cos(90))
print(math.tan(90))