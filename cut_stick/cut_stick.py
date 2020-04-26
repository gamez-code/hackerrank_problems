def cut_filter(arr):
    min_arr = min(arr)
    result = list(filter(lambda x: x > 0, map(lambda x: x - min_arr, arr)))
    return result


def cutTheSticks(arr):
    result = []
    while arr:
        result.append(len(arr))
        arr = cut_filter(arr)
    else:
        return result



def cutTheSticks0(arr):
    if arr:
        min_arr = min(arr)
        result = [len(arr)]
        arr = list(filter(lambda x: x > 0, map(lambda x: x - min_arr, arr)))
        return result + cutTheSticks0(arr)
    else:
        return arr


if __name__ == '__main__':
    arr = '5 4 4 2 2 8'
    arr = list(map(int, arr.split()))
    print(cutTheSticks0(arr))
