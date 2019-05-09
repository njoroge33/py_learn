import pytest
from ..raising__exceptions import length, LengthError


def test_length_raised_exception():
    with pytest.raises(LengthError):
        length('th')

def test_length_raised_exception_with_message():
    with pytest.raises(LengthError) as err:
        length('th')
        assert err == 'String too short'
