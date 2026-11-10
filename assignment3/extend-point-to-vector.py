import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def distance(self, other):
        return math.sqrt(
            (self.x - other.x) ** 2 +
            (self.y - other.y) ** 2
        )


class Vector(Point):
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)


point1 = Point(3, 4)
point2 = Point(7, 2)
point3 = Point(3, 4)

vector1 = Vector(1, 2)
vector2 = Vector(3, 4)

print(point1)
print(point1 == point2)
print(point1.distance(point3))

print(vector1)
print(vector1 + vector2)
