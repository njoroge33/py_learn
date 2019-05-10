import pytest
from ..red_lottery_ticket import find_ticket_value


@pytest.mark.parametrize('a, b, c, expected', [
    (2, 2, 2, 10),
    (1, 1, 1, 5),
    (0, 2, 1, 1),
    (2, 0, 1, 1),
    (2, 0, 2, 0),
    (0, 0, 2, 0),
    (1, 1, 2, 0)
])
def test_find_ticket_value(a, b, c, expected):
    actual = find_ticket_value(a, b, c)
    assert actual == expected
