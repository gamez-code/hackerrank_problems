# Complete the happyLadybugs function below.
def happyLadybugs(b):
    n = len(b)
    for a in set(b):
        if a != "_" and b.count(a) == 1:
            return "NO"

    if b.count("_") == 0:
        for i in range(1, n - 1):
            if b[i - 1] != b[i] and b[i + 1] != b[i]:
                return "NO"
    return "YES"


if __name__ == '__main__':
    print(happyLadybugs('A_TOJRPRW__JOJP__WAJT'))
    """
    with open('data.txt', 'r') as file:
        data = file.readlines()

    g = int(data[0])

    for g_itr in range(1, g * 2, 2):
        n = data[g_itr]

        b = data[g_itr + 1].replace('\n', '')

        result = happyLadybugs(b)

        with open('output.txt', 'a') as file:
            file.write(result + '\n')
    """
