import math

a = int(input("Enter coefficient of x-squared: "))
b = int(input("Enter coefficient of x: "))
c = int(input("Enter coefficient of units: "))

discriminant = b ** 2 - 4 * a * c
denominator  = 2 * a

if discriminant >= 0:
    part2 = math.sqrt(discriminant)     
    root1 = (-b + part2)/denominator
    root2 = (-b - part2)/denominator
else:
    imag = math.sqrt(-discriminant) / denominator
    root1 = complex(-b/denominator, +imag)
    root2 = complex(-b/denominator, -imag)

print("Root 1 : %s" % root1)
print("Root 2 : %s" % root2)

    
