import math


def squares(a, b):
    ab = range(a, b + 1)
    ab22 = list(map(lambda x: int(math.pow(x, 2)), range(math.ceil(math.sqrt(a)), math.ceil(math.sqrt(b)) + 1)))
    sab = sum(map(lambda x: x in ab, ab22))
    return sab


if __name__ == '__main__':
    a = 24
    b = 49
    print(squares(a, b))
