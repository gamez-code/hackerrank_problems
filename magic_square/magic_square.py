#!/bin/python3

import math
import os
import random
import re
import sys


def sum_row(_s):
    _result = list(map(sum, _s))
    return _result


def sum_column(_s, column):
    _result = sum(map(lambda x: x[column], _s))
    return _result


def sum_columns(_s):
    return [sum_column(_s, i) for i in range(len(_s[0]))]


def sum_diagonal(_s):
    accumulator_1, accumulator_2 = 0, 0
    for i in range(len(_s)):
        accumulator_1 += _s[i][i]
        accumulator_2 += _s[i][- i - 1]
    else:
        return [accumulator_1, accumulator_2]


def select_magic_constant(_rows, _column, _diagonal, _total):
    magic_one = (0, 0)
    for magic_constant in _total[1]:
        aux = sum([_rows.count(magic_constant), _column.count(magic_constant), _diagonal.count(magic_constant)])
        if aux > magic_one[1]:
            magic_one = (magic_constant, aux)
    else:
        return magic_one[0]

def ajust_diagonal(_s, _diagonal, target):
    if _diagonal[0] > target:
        pass
    else:
        pass

def ajust_columns(_s, _column, target):
    pass

def ajust_row(_s, _rows, target):
    if _rows[0] > target:

    pass

def ajust(_s, target, *args):
    _rows, _column, _diagonal, _total = args
    if not all(map(lambda x: target is x, _diagonal)):
        return ajust_diagonal(_s, _diagonal, target)
    elif not all(map(lambda x: target is x, _column)):
        return ajust_columns(_s, _column, target)
    elif not all(map(lambda x: target is x, _rows)):
        return ajust_row(_s, _rows, target)


def verify(_s):
    _rows = sum_row(_s)
    _column = sum_columns(_s)
    _diagonal = sum_diagonal(_s)
    _total = set(_rows + _column + _diagonal)
    if len(_total) == 1:
        return True, (_rows, _column, _diagonal, _total)
    else:
        return False, (_rows, _column, _diagonal, _total)

def recursive_magic(_s):
    is_ok, args = verify(s)
    if is_ok:
        return _s
    else:
        magic_constant = select_magic_constant(*args)
        _s = ajust(_s, magic_constant, *args)
        return recursive_magic(_s)
# Complete the formingMagicSquare function below.

def formingMagicSquare(s):
    # Column sum




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    # result = formingMagicSquare(s)

    # fptr.write(str(result) + '\n')

    # fptr.close()
