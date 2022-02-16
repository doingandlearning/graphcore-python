import math

while True:
    try:
        r = float(input("Enter radius: "))
        break
    except ValueError as err:
        print(f"Whoops! {err}")


diameter      = 2 * r
circle_area   = math.pi * r ** 2
circumference = math.pi * diameter

print("Circle values: %g %g %g" % (diameter, circle_area, circumference))

sphere_area   = 4 * math.pi * r ** 2
sphere_volume = (4/3) * math.pi * r ** 3

print("Sphere values: %g %g" % (sphere_area, sphere_volume))