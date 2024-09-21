from src.figure import Figure


class Circle(Figure):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Радиус окружности не может быть меньше нуля!")
        self.radius = radius


    @property
    def get_perimeter(self):
        return 2 * 3.14 * self.radius


    @property
    def get_area(self):
        return 3.14 * (self.radius**2)



