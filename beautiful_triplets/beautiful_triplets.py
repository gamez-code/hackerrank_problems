def fun(i, d, a, n):
    acum = 0
    ji = 1
    for j in range(1 + i, n):
        if ji > d:
            return acum
        for k in range(1 + j, n):
            ji = a[j] - a[i]
            kj = a[k] - a[j]
            if kj > d:
                break
            if ji == d and kj == d:
                acum += 1
            elif ji > d and kj > d:
                return acum
    else:
        return acum


def beautifulTriplets(d, a):
    n = len(a)
    acum = sum(map(lambda i: fun(i, d, a, n), range(n)))

    return acum


if __name__ == '__main__':
    d = 3
    arr = [1, 2, 4, 5, 7, 8, 10]
    print(beautifulTriplets(d, arr))
    with open('data.txt', 'r') as file:
        arr = list(map(int, file.read().split()))

    #print(beautifulTriplets(d, arr))
    #print(beautifulTriplets(d, arr) == 9996)
