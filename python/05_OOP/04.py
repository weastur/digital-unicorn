import math

class Figure:

    def area(self):
        pass

    def perimeter(self):
        pass

    def info(self):
        print(f"Area - {self.area()}")
        print(f"Perimeter - {self.perimeter()}")


class Rectangle(Figure):

    def __init__(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

    def area(self):
        return abs(self._x1 - self._x2) * abs(self._y1 - self._y2)

    def perimeter(self):
        return 2 * (abs(self._x1 - self._x2) + abs(self._y1 - self._y2))


class Triangle(Figure):

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._x3 = x3
        self._y3 = y3

    def area(self):
        p = self.perimeter() / 2
        a = self._len(self._x1, self._y1, self._x2, self._y2)
        b = self._len(self._x3, self._y3, self._x2, self._y2)
        c = self._len(self._x1, self._y1, self._x3, self._y3)
        return math.sqrt(p * (p - a) * (p - b) * (p - c))

    def perimeter(self):
        return self._len(self._x1, self._y1, self._x2, self._y2) + self._len(self._x1, self._y1, self._x3, self._y3) + self._len(self._x2, self._y2, self._x3, self._y3)

    def _len(self, x1, y1, x2, y2):
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


class Circle(Figure):

    def __init__(self, x1, y1, r):
        self._x1 = x1
        self._y1 = y1
        self._r = r

    def area(self):
        return math.pi * (self._r ** 2)

    def perimeter(self):
        return 2 * math.pi * self._r


figures = [Rectangle(1, 1, 10, 10), Circle(1, 1, 10), Triangle(1, 1, 5, 10, 10, 5)]

for figure in figures:
    figure.info()