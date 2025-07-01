class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum_points(self, p):
        return Point((self.x + p.x), (self.y + p.y))

    def print_point(self):
        return (self.x, self.y)

    def __add__(self, p):
        return Point((self.x + p.x), (self.y + p.y))

    def __sub__(self, p):
        return Point((self.x - p.x), (self.y - p.y))


p1 = Point(1, 2)
p2 = Point(2, 4)

# p = p1.sum_points(p2)
# print(p.print_point())
p = p1 - p2
print(p.print_point())
