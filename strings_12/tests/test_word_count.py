import pytest
from ..word_count import len_word


@pytest.mark.parametrize("x_str, expected", [
    ("robbin is there", "robbin"),
    ("am on the ground", "ground"),
    ("i don't greet people", "people")
])
def test_word_count(x_str, expected):
    actual = len_word(x_str)
    assert actual == expected
