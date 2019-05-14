import pytest
from ..devry_admission_program import is_admitted


@pytest.mark.parametrize('gpa, sat, expected', [
    (1.8, 899, False),
    (2, 899, False),
    (3, 1010, True)
])
def test_is_admitted(gpa, sat, expected):
    actual = is_admitted(gpa, sat)
    assert actual == expected
