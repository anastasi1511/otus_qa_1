from src.Rectangle import Rectangle

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


