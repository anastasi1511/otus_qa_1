from src.Square import Square

import pytest


@pytest.mark.parametrize(
    "side_a, side_b, area",
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
