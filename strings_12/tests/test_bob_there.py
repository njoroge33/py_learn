import pytest
from ..bob_there import bob_there


@pytest.mark.parametrize("x_str, expected", [
    ("robbin", False),
    ("bob", True),
    ("baba", True)
])
def test_bob_there(x_str, expected):
    actual = bob_there(x_str)
    assert actual == expected
