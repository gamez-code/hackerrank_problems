# Complete the stones function below.

def stones(n, a, b):
    acum = []
    ran = list(range(n))
    for j in ran[::-1]:
        for i in ran:
            if i + j == n - 1:
                acum.append(a * i + b * j)

    result = set(acum)
    return sorted(result)


if __name__ == '__main__':
    n = 3
    a = 1
    b = 2
    result = stones(n, a, b)
    print(result)
    """
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        n = int(input())

        a = int(input())

        b = int(input())

        result = stones(n, a, b)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
    """
