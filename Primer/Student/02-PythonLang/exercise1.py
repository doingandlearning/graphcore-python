import math

radius = float(input("What is the radius? "))
diameter = radius * 2
area = math.pi * pow(radius, 2)
circumference = math.pi * diameter
surface_area_of_sphere = 4 * math.pi * (radius ** 2)
volume_of_sphere = (4/3) * math.pi * (radius ** 3)

print(f"""
You entered the radius {radius}.

Circle:
- Diameter: {diameter}
- Area: {area}
- Circumference: {circumference}

Sphere:
- Surface Area: {surface_area_of_sphere:.2f}
- Volume: {volume_of_sphere:.2f}
""")