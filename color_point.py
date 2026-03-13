from point import Point

class ColorPoint(Point):
    """
    Color point class inherits from Point class.
    """
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

p1 = ColorPoint(1, 2, 'red')
print(p1.color)
print(p1)