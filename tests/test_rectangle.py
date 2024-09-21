from src.rectangle import Rectangle
from src.square import Square
import pytest


@pytest.mark.parametrize(
    "side_a, side_b, area",
    [
        (3, 5, 15),
        (3.5, 5.5, 19.25)
    ],
    ids=["integer", "float"]
)
def test_rectangle_area_positive(side_a, side_b, area):
    x = Rectangle(side_a, side_b)
    assert x.get_area == area, f'Area should be {area}'


@pytest.mark.parametrize(
    "side_a, side_b, perimeter",
    [
        (3, 5, 16),
        (3.5, 5.5, 18)
    ],
    ids=["integer", "float"]
)
def test_rectangle_perimeter_positive(side_a, side_b, perimeter):
    x = Rectangle(side_a, side_b)
    assert x.get_perimeter == perimeter, f'Perimeter should be {perimeter}'


@pytest.mark.parametrize(
    "side_a, side_b, add_area",
    [
        (10, 7, 170),
        (10.5, 7.5, 189)
    ],
    ids=["integer", "float"]
)
def test_rectangle_add_area_positive(side_a, side_b, add_area):
    x = Rectangle(side_a, side_b)
    y = Square(side_a)
    assert x.add_area(y) == add_area, f'Add_area should be {add_area}'


@pytest.mark.parametrize(
    "side_a, side_b",
    [
        (0, 0),
        (-1, -5)
    ],
    ids=["sides are zero", "sides less than zero"]
)
def test_rectangle_sides_negative(side_a, side_b):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)


@pytest.mark.parametrize(
    "side_a, side_b",
    [
        (20, 0)
    ],
    ids=["side_b = 0"]
)
def test_square_add_area_negative(side_a, side_b):
    with pytest.raises(ValueError):
        x = Rectangle(side_a, side_b)
        y = Square(side_a)
        x.add_area(y)
