import pytest
from ..reverse_the_sentence import reverse_str


@pytest.mark.parametrize("x_str, expected", [
    ("robbin", "nibbor"),
    ("bob", "bob"),
    ("baba", "abab")
])
def test_reverse_str(x_str, expected):
    actual = reverse_str(x_str)
    assert actual == expected
