def jumpingOnClouds(c, k, i=0):
    i += k
    if i >= len(c):
        i = i % len(c)
        if i == 0:
            if c[0] == 0:
                return -1 + 100
            else:
                return -3 + 100
        else:
            if c[i] == 0:
                return -1 + jumpingOnClouds(c, k, i)
            else:
                return -3 + jumpingOnClouds(c, k, i)
    else:
        if c[i] == 0:
            return -1 + jumpingOnClouds(c, k, i)
        else:
            return -3 + jumpingOnClouds(c, k, i)


if __name__ == '__main__':
    c = '0 0 1 0 0 1 1 0'
    c = list(map(int, c.split()))
    k = 2
    print(jumpingOnClouds(c, k))
