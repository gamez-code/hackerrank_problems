def jumpingOnClouds(c, i=0):
    if i == len(c) - 1:
        return 0
    elif i + 2 <= len(c) - 1 and c[i + 2] == 0:
        i += 2
    elif i + 1 <= len(c) - 1 and c[i + 1] == 0:
        i += 1

    return 1 + jumpingOnClouds(c, i)


if __name__ == '__main__':
    c = '0 0 0 0 1 0'
    c = list(map(int, c.split()))
    print(jumpingOnClouds(c))
