import pytest


def appendAndDelete(s, t, k):
    for i in range(1, len(t) + 1):
        if t[:i] not in s:
            _delete = len(t) - i + 1
            if _delete > k:
                return 'No'
            else:
                _append = len(s) - i + 1
                if len(s) < len(t) and not s.count(t[0]) == len(s):
                    _append = 2 * len(s) + 1 if _append == 0 else _append
                if _delete + _append <= k:
                    return 'Yes'
                else:
                    return 'No'
    if len(t) > len(s):
        _delete = len(t) + 1
        _append = len(t)
        if _delete + _append <= k:
            return 'Yes'
        else:
            return 'No'
    elif len(t) == len(s):
        return 'Yes'
    else:
        _append = len(s) - i + 1
        if _append <= k:
            return 'Yes'
        else:
            return 'No'


@pytest.mark.parametrize(
    "s,t,k,expected",
    [('hackerhappy', 'hackerrank', 9, 'Yes'), ('aba', 'aba', 7, 'Yes'), ('ashley', 'ash', 2, 'No'),
     ('asdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcv',
      'asdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcv',
      20, 'Yes'), ('zzzzz',
                   'zzzzzzz',
                   4, 'Yes'), ('abcd',
                               'abcdert',
                               10, 'No')],
)
def test_appendAndDelete(s, t, k, expected):
    assert (appendAndDelete(s, t, k) == expected)


if __name__ == '__main__':
    print(appendAndDelete(
        'zzzzz',
        'zzzzzzz',
        4))
