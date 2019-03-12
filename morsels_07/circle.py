import math


class Circle(object):
    def __init__(self, radius=1):
        self._radius = None
        self.radius = radius

    def __repr__(self) -> str:
        return f'Circle({self.radius})'

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, d):
        self.radius = d / 2

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        if r < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = r

    @property
    def area(self):
        return self.radius ** 2 * math.pi