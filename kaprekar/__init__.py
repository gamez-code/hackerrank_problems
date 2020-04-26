def fun(a):
    num = str(pow(a, 2))
    num_left = num[len(num) // 2::]
    num_right = num[:len(num) // 2]
    num_right = '0' if num_right == '' else num_right
    if int(num_left) + int(num_right) == a:
        return a
    else:
        return 0


def kaprekarNumbers(p, q):
    result = list(filter(lambda x: x > 0, map(fun, range(p, q + 1))))
    if sum(result):
        return result
    else:
        return 'INVALID RANGE'


if __name__ == '__main__':
    print(kaprekarNumbers(1, 100))
