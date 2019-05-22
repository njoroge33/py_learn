import pytest
from ..find_an_alphabet_and_count_it import alphabet_count


@pytest.mark.parametrize("x_string, alphabet, expected", [
    ("hae", "j", False),
    ("opinion", "i", (2, 4, 2)),
    ("opinion", "n", 3, 6, 2),
])
def test_alphabet_count(x_string, alphabet, expected):
    actual = alphabet_count(x_string, alphabet)
    assert actual == expected
