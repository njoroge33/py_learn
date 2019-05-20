import pytest

from ..sexy_pairs import get_sexy_pairs


@pytest.mark.parametrize('limit, expected', [
    (12, [(5, 11)]),
    (20, [(5, 11), (7, 13), (11, 17), (13, 19)]),
    (32, [(5, 11), (7, 13), (11, 17), (13, 19), (17, 23), (23, 29)])
])
def test_get_sexy_pairs(limit, expected):
    actual = get_sexy_pairs(limit)
    assert actual == expected
