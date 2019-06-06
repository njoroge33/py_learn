import pytest
from ..word_count import len_word


@pytest.mark.parametrize("x_str, expected", [
    ("robbin", 6),
    ("bob", 3),
    ("baba", 4)
])
def test_word_count(x_str, expected):
    actual = len_word(x_str)
    assert actual == expected
