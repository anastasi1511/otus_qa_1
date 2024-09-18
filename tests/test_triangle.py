from src.triangle import Triangle
from src.circle import Circle

import pytest


@pytest.mark.parametrize(
    "side_a, side_b, side_f, area",
    [
        (5, 3, 7, 6.49519052838329),
        (5.5, 3.5, 7.5, 8.990229071052639)
    ],
    ids=["integer", "float"]
)
def test_triangle_area_positive(side_a, side_b, side_f, area):
    x = Triangle(side_a, side_b, side_f)
    assert x.get_area == area, f'Area should be {area}'


@pytest.mark.parametrize(
    "side_a, side_b, side_f, perimeter",
    [
        (5, 3, 7, 15),
        (5.5, 3.5, 7.5, 16.5)
    ],
    ids=["integer", "float"]
)
def test_triangle_perimeter_positive(side_a, side_b, side_f, perimeter):
    x = Triangle(side_a, side_b, side_f)
    assert x.get_perimeter == perimeter, f'Perimeter should be {perimeter}'


@pytest.mark.parametrize(
    "side_a, side_b, side_f, radius, add_area",
    [
        (10, 7, 12, 11, 414.91767144908306),
        (10.5, 7.5, 12.5, 11.5, 454.55652858759765)
    ],
    ids=["integer", "float"]
)
def test_triangle_add_area_positive(side_a, side_b, side_f, radius, add_area):
    x = Triangle(side_a, side_b, side_f)
    y = Circle(radius)
    assert x.add_area(y) == add_area, f'Add_area should be {add_area}'


@pytest.mark.parametrize(
    "side_a, side_b, side_f",
    [
        (7, 1, 18),
        (7, 11, 18)
    ],
    ids=["the sum of the sides is less than a third", "the sum of the sides is equal to the third"]
)
def test_triangle_sides_negative(side_a, side_b, side_f):
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_f)

