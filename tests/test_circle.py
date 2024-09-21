from src.circle import Circle

from src.square import Square

from src.figure import Figure

import pytest


@pytest.mark.parametrize(
    "radius, area",
    [
        (5, 78.5),
        (5.5, 94.985)
    ],
    ids=["integer", "float"]
)
def test_circle_area_positive(radius, area):
    x = Circle(radius)
    assert x.get_area == area, f'Area should be {area}'


@pytest.mark.parametrize(
    "radius, perimeter",
    [
        (5, 31.400000000000002),
        (5.5, 34.54)
    ],
    ids=["integer", "float"]
)
def test_circle_perimeter_positive(radius, perimeter):
    x = Circle(radius)
    assert x.get_perimeter == perimeter, f'Perimeter should be {perimeter}'


@pytest.mark.parametrize(
    "radius, side_a, add_area",
    [
        (10, 7, 363),
        (10.5, 7.5, 402.435)
    ],
    ids=["integer", "float"]
)
def test_circle_add_area_positive(radius, side_a, add_area):
    x = Circle(radius)
    y = Square(side_a)
    assert x.add_area(y) == add_area, f'Add_area should be {add_area}'


@pytest.mark.parametrize(
    "radius",
    [
        0, -1,
    ],
    ids=["radius=0", "radius<0"]
)
def test_circle_radius_negative(radius):
    with pytest.raises(ValueError):
        Circle(radius)


@pytest.mark.parametrize(
    "radius, not_figure",
    [
        (5, 7)
    ],
    ids=["The second object is not figure"]
)
def test_square_add_area_negative(radius, not_figure):
    y = Circle(radius)
    with pytest.raises(ValueError):
        y.add_area(not_figure)
