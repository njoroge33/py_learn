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


def test_is_admitted_raises_error():
    with pytest.raises(ValueError) as err:
        is_admitted('not a number', 'sat')
        assert err
