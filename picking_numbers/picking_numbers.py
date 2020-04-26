def pickingNumbers(a):
    # Write your code here
    # result = max(list(map(lambda y: len(list(filter(lambda x: abs(x - y) == 1 or abs(x - y) == 0, a))), a)))
    # results = list(map(lambda y: list(filter(lambda x: abs(x - y) == 1 or abs(x - y) == 0, a)), a))
    result = []
    for i in range(len(a)):
        result.append([])
        for _a in a:
            if abs(a[i] - _a) in [0, 1]:
                if all(map(lambda x: abs(x - _a) in [0, 1], result[i])):
                    result[i].append(_a)

    else:
        result = max(map(len, result))
        return result


if __name__ == '__main__':
    a = '4 6 5 3 3 1'
    a = list(map(int, a.split()))
    print(pickingNumbers(a))
