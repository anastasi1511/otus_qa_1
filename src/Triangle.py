import math

from src.Figure import Figure


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_f):
        if side_a <= 0 or side_b <= 0 or side_f <= 0:
            raise ValueError("не может быть треугольника со стороной меньше нуля!")
        if (side_a + side_f <= side_b) or (side_a + side_b <= side_f) or (side_f + side_b <= side_a):
            raise ValueError("У треугольника сумма любых двух сторон должна быть больше третьей!")
        self.side_a = side_a
        self.side_b = side_b
        self.side_f = side_f

    @property
    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_f

    @property
    def get_perimeter_half(self):
        return self.get_perimeter / 2

    @property
    def get_area(self):
        return math.sqrt(
            (self.get_perimeter_half * (self.get_perimeter_half - self.side_a) * (self.get_perimeter_half - self.side_b)
             * (self.get_perimeter_half - self.side_f)))



