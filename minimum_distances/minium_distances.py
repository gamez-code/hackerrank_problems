def minimumDistances(a):
    distances = []
    for i in range(len(a)):
        if a.count(a[i]) > 1:
            for j in range(i + 1, len(a)):
                if a[i] == a[j]:
                    distances.append(j - i)
                    break
    else:
        if distances:
            return min(distances)
        else:
            return -1


if __name__ == '__main__':
    a = '7 1 3 4 1 7'
    a = a.split()
    print(minimumDistances(a))
