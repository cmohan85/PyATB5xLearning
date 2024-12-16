# Triangle Classifier
#  w.a.p that classifies a triangle based on its side lengths.


def classify_triangle(a,b,c):
    if a > 0 and b > 0 and c > 0:
        if a + b > c and b + c > a and a + c > b:
            if a == b == c:
                return "Equilateral"
            elif a == b or b == c or a == c:
             return "Isosceles"
            else:
                return "Scalene"
        else:
            print('Not a Triangle')
    else:
        print("Not a valid length")

side1 = int(input('Enter the first side'))
side2 = int(input('Enter the second side'))
side3 = int(input('Enter the third side'))

result = classify_triangle(side1,side2,side3)
print(f'This triangle is classified as: {result}')