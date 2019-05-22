import pytest
from ..recursive_functions import fact


@pytest.mark.parametrize('num, expected', [
    (5, 120),
    (6, 720),
    (0, 1)
])
def test_recursive_functions(num, expected):
    actual = fact(num)
    assert actual == expected
