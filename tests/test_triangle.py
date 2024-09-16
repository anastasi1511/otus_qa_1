from src.Triangle import Triangle

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