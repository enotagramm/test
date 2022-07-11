import math as mt


class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def get_len(self, other):
        self.x = self.x - other.x
        self.y = self.y - other.y
        l1 = mt.sqrt((self.x ** 2) + (self.y ** 2))
        return l1


pt1 = Point(0, 0)
pt2 = Point(3, 4)
print(Point.get_len(pt1, pt2))


