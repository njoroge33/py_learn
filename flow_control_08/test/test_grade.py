import pytest
from ..grade import gen_report


@pytest.mark.parametrize('marks, expected', [
    (dict(kisw=34, eng=50), dict(kisw='FAIL', eng='C', average='D')),
    (dict(kisw=34, eng=50), dict(kisw='FAIL', eng='C', average='D')),
    (dict(kisw=34, eng=50), dict(kisw='FAIL', eng='C', average='D'))
])
def test_grade(marks, expected):
    actual = gen_report(marks)
    assert actual == expected
