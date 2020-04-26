#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    # acum = max(map(lambda city: min([abs(city - _c) for _c in c]), range(n)))
    # acum = max(map(lambda city: min(map(lambda _c: abs(city - _c), c)), range(n)))
    c.sort()
    acum = 0
    for i in range(len(c) - 1):
        aux = c[i+1] - c[i]
        if aux > acum:
            acum = aux
    else:
        if n - c[-1] > acum and n - c[-1] > c[0]:
            return n - c[-1] - 1
        elif c[0] > acum:
            return c[0]
        else:
            return acum // 2




if __name__ == '__main__':
    with open('data.txt', 'r') as file:
        data = file.readlines()

    nm = data[0].split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, data[1].rstrip().split()))
    n = 99998
    m = 5
    c = [28000,
    58701,
    43043,
    24909,
    28572]


    n = 99989
    m = 4
    c=[75453,
    36129,
    64502,
    46817]

    result = flatlandSpaceStations(n, c)

    print(result)
