def circularArrayRotation(a, k, queries):
    n = len(a)
    if n > k:
        i = n - k
        a = a[i::] + a[:i]
    elif n < k:
        i = n - k % n
        a = a[i::] + a[:i]
    a = a[335::] + a[:335]
    return map(lambda q: a[q], queries)


if __name__ == '__main__':
    a = [1, 2, 3]
    k = 2
    queries = [0, 1, 2]
    with open('data_2.txt', 'r') as file:
        lines = file.readlines()

    n, k, q = list(map(int, lines[0].split()))

    a = list(map(int, lines[1].rstrip().split()))

    queries = map(int, lines[2::])
    result = list(circularArrayRotation(a, k, queries))

    with open('data_2_expected.txt', 'r') as file:
        expected = file.readlines()

    print(result[:20])