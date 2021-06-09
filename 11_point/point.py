class Point(object):

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def __repr__(self):
        return f"Point({self.x}, {self.y}, {self.z})"

    def __mul__(self, multiplier):
        return Point(self.x * multiplier, self.y * multiplier, self.z * multiplier)

    def __rmul__(self, multiplier):
        return self.__mul__(multiplier)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def __iter__(self):
        return iter([self.x, self.y, self.z])
