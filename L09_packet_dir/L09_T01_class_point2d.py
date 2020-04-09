# Пример класса по определению расстояния до указанных координат на плоскости начиная с пересечения осей x и y (0)
#-----------------------------------------------------------------------------------------------------------------
# по соглашению программистов, имена классов пишутся с Большой буквы
class Point2D:
    # Стандартный МЕТОД, Инициализации АТРИБУТОВ класса
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Стандартный МЕТОД, вывод, который будет выполнятся в команде print
    def __str__(self):
        # команда: "print(Point2D(4,3))" выдаст: "крд.точки: (4, 3)"
        return f'крд.точки: ({self.x}, {self.y})'

    # обработка данных в классе - расчёт 1
    # Стандартный МЕТОД, перегрузка "+", возможность сложения координат в print
    def __add__(self, other):
        # команда: "print(Point2D(4,3)+Point2D(-4,-3))" выдаст: "крд.точки: (0, 0)"
        return Point2D(self.x + other.x, self.y + other.y)
    # обработка данных в классе - расчёт 2
    def distance(self):
        return (self.x**2 + self.y**2 )**0.5
    # обработка данных в классе - расчёт 3
    def point_distance(self, a, b):
        return ((self.x-a)**2 + (self.y-b)**2 )**0.5
#-----------------------------------------------------------------------------------------------------------------
# Ввод значений данных для обработки
p = Point2D(4,3)
q = Point2D(-4,-3)
# Операции со значениями данных и вывод результа:
print('# Результат:')
print('# I точка "p",',p )
print('# I точка "p", вариант 2 вывода координат - "p.x, p.y":', p.x, p.y)
print('# II точка "q",',q )
print('# расчёт 1, сумма координат двух точек:')
print('#', p+q)
print('# расчёт 2, расстояние до координат точки "p" на плоскости начиная с пересечения осей x и y (точки "0"):')
print('#', p.distance())
print('# расчёт 3, расстояния от координат точки "p" до указанных координат выполняется вызовом функции класса:')
print('#', p.point_distance(4,7))