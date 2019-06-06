import pytest
from ..count_triplets import count_triplets


@pytest.mark.parametrize("x_str, expected", [
    ("jjjjjjkkkohn", 3),
    ("crosssection", 1),
    ("cross", False)
])
def test_count_triplets(x_str, expected):
    actual = count_triplets(x_str)
    assert actual == expected
