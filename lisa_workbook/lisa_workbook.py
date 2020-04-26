def workbook(n, k, arr):
    # pages = [math.ceil(arr[chapter] / k) for chapter in range(n)]
    pages = 0
    special = 0
    for chapter in range(n):
        accum = 0
        pages += 1
        for problem in range(1, 1 + arr[chapter]):
            accum += 1
            if pages == problem:
                special += 1
            if accum == k and arr[chapter] != problem:
                accum = 0
                pages += 1
    return special


n, k = 5, 3
arr = [4, 2, 6, 1, 10]
if __name__ == '__main__':
    print(workbook(n, k, arr))
