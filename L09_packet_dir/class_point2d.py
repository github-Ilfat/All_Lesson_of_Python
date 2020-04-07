class Point2D:
    # инициализации
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # вывод
    def __str__(self):
        return f'Точка: ({self.x}, {self.y})'
    # перегрузка "+"
    def __add__(self, other):
        return Point2D(self.x + other.x, self.y + other.y)


    def distance(self):
        return (self.x**2 + self.y**2 )**0.5

    def point_distance(self, a, b):
        return ((self.x-a)**2 + (self.y-b)**2 )**0.5



p = Point2D(2,3)
q = Point2D(3,-2)

print(p+q)
print(p.x, p.y)
print(p)
print(p.distance())
print(p.point_distance(3,4))