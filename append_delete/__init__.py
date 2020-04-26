import pytest


def appendAndDelete(s, t, k):
    for i in range(1, len(t)):
        if t[::i] not in s:
            break
    else:
        _delete = len(t) - i - 1
        if _delete > k:
            return 'No'
        else:
            _append = len(s) - i - 1
            if _delete + _append <= k:
                return 'Yes'
            else:
                return 'No'


@pytest.mark.parametrize(
    "s,t,k,expected",
    [('hackerhappy', 'hackerrank', 9, 'Yes'), ('aba', 'aba', 7, 'Yes'), ('ashley', 'ash', 2, 'No')],
)
def test_appendAndDelete(s, t, k, expected):
    assert (appendAndDelete(s, t, k) == expected)
