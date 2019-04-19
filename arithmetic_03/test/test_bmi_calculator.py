import pytest

from ..bmi_calculator import bmi_calculator


@pytest.mark.parametrize('weight, height, expected', [
    (20, 1.3, 11.83),
    (100, 1.5, 44.44),
    (150, 1.8, 46.29)
])
def test_bmi_calculator(weight, height, expected):
    actual = bmi_calculator(weight, height)
    assert actual == expected
