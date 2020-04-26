def pageCount1(n, p):
    #
    # Write your code here.
    #
    rest_np = n - p
    if p > (rest_np):
        return int(rest_np / 2)
    else:
        return int(p / 2)


def pageCount(n, p):
    #
    # Write your code here.
    #
    list_flip = [(i, i + 1) for i in range(0, n + 1, 2)]
    list_flip_reverse = list_flip.copy()
    list_flip_reverse.reverse()
    element = list(filter(lambda x: p in x, list_flip))
    front = list_flip.index(element[0])
    back = list_flip_reverse.index(element[0])
    if front > back:
        return back
    else:
        return front


if __name__ == '__main__':
    n, p = 6, 2
    print(pageCount(n, p))
