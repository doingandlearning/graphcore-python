import math

class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return (f'Pizza({self.radius!r}, '
                f'{self.ingredients!r})')

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi

    @classmethod
    def cheese (cls, radius):
        return cls(radius, "cheese")

cheesePizza = Pizza.cheese(9)
cheesePizza2 = Pizza(9, "cheese")

print(cheesePizza)
print(cheesePizza2)


