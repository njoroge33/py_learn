import pytest
from ..evenly_spaced import evenly_spaced


@pytest.mark.parametrize('a, b, c, expected', [
    (10, 20, 30, True),
    (50, 100, 200, False),
    (32.5, 60, 87.5, True)
])
def test_evenly_spaced(a, b, c, expected):
    actual = evenly_spaced(a, b, c)
    assert actual == expected


def test_evenly_spaced_raises_error():
    with pytest.raises(ValueError) as err:
        evenly_spaced('a', 'b', 'c')
        assert err
