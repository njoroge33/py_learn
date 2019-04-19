import pytest

from ..convert_days_to_years_weeks_and_days_passed import days_to_years_weeks_days


@pytest.mark.parametrize('days, expected', [
    (375, (1, 1, 3)),
    (240, (0, 34, 2)),
    (765, (2, 5, 0)),
    (771, (2, 5, 6))
])
def test_days_to_years_weeks_days(days, expected):
    actual = days_to_years_weeks_days(days)
    assert actual == expected
