

def cavityMap(grid):
    grid = [[j for j in i] for i in grid]
    n = len(grid) - 1
    for row in range(len(grid)):
        if row == 0 or row == n:
            continue
        for column in range(len(grid[row])):
            element = grid[row][column]
            if column == 0 or column == n:
                continue
            if grid[row - 1][column] < element and grid[row + 1][column] < element and grid[row][column - 1] < element and grid[row][column + 1] < element:
                grid[row][column] = 'X'
    grid = [''.join(i) for i in grid]
    return grid


if __name__ == '__main__':
    case1 = ['1112', '1912', '1892', '1234']
    case2 = ['12', '12']
    print(cavityMap(case1))
