import pytest
from ..reverse_the_sentence import reverse_str


@pytest.mark.parametrize("x_str, expected", [
    ("robbin is there", "there is robbin"),
    ("bob sang", "sang bob"),
    ("here is an example", "example an is here")
])
def test_reverse_str(x_str, expected):
    actual = reverse_str(x_str)
    assert actual == expected
