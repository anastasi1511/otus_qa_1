from src.Circle import Circle

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