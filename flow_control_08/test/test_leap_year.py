import pytest
from ..leap_year import is_leap_year


@pytest.mark.parametrize('year, expected', [
    (2012, True),
    (1989, False),
    (2000, True)
])
def test_is_leap_year(year, expected):
    actual = is_leap_year(year)
    assert actual == expected
