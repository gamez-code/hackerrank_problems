def give_candy(n, candys, index):
    if candys == 0:
        return index
    else:
        if index == n:
            index = 1
        else:
            index += 1
        return give_candy(n, candys - 1, index)


def saveThePrisoner(n, m, s):
    """
    :param n: the number of prisoners
    :param m: the number of sweets
    :param s: the chair number to start passing out treats at
    :return:
    """
    res = m % n
    if res and res + s - 1 <= n:
        return res + s - 1
    else:
        return s - 1


if __name__ == '__main__':
    n, m, s = list(map(int, '5 2 2'.split()))
    print(saveThePrisoner(n, m, s))
