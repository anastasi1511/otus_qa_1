from src.square import Square
from src.rectangle import Rectangle

import pytest


@pytest.mark.parametrize(
    "side_a, area",
    [
        (5, 25),
        (5.5, 30.25)
    ],
    ids=["integer", "float"]
)
def test_square_area_positive(side_a, area):
    x = Square(side_a)
    assert x.get_area == area, f'Area should be {area}'


@pytest.mark.parametrize(
    "side_a, perimeter",
    [
        (5, 20),
        (5.5, 22)
    ],
    ids=["integer", "float"]
)
def test_square_perimeter_positive(side_a, perimeter):
    x = Square(side_a)
    assert x.get_perimeter == perimeter, f'Perimeter should be {perimeter}'


@pytest.mark.parametrize(
    "side_a, side_b, add_area",
    [
        (10, 7, 170),
        (10.5, 7.5, 189)
    ],
    ids=["integer", "float"]
)
def test_square_add_area_positive(side_a, side_b, add_area):
    x = Rectangle(side_a, side_b)
    y = Square(side_a)
    assert x.add_area(y) == add_area, f'Add_area should be {add_area}'


@pytest.mark.parametrize(
    "side_a",
    [
        0, -22
    ],
    ids=["side is zero", "side less than zero"]
)
def test_square_side_negative(side_a):
    with pytest.raises(ValueError):
        Square(side_a)


@pytest.mark.parametrize(
    "side_a, not_figure",
    [
        (20, 7)
    ],
    ids=["The second object is not figure"]
)
def test_square_add_area_negative(side_a, not_figure):
    y = Square(side_a)
    with pytest.raises(ValueError):
        y.add_area(not_figure)