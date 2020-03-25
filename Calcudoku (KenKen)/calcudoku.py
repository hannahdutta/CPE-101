# Name:         Parth Ray
# Course:       CPE 101
# Instructor:   Daniel Kauffman
# Assignment:   Calcudoku
# Term:         Fall 2019

def main():
    cage_list = get_cage_list()
    grid = create_grid(cage_list)
    grid_1d = [j for i in grid for j in i]
    i = 0
    while i < len(grid_1d):
        grid_1d[i] += 1
        grid = grid1d_to_2d(grid_1d)
        if grid_1d[i] > len(grid):
            grid_1d[i] = 0
            i -= 1
        elif check_cages(grid, cage_list) and check_lines(grid):
            i += 1
    display_solution(grid1d_to_2d(grid_1d))


def check_cages(grid, cage_list):
    for i in cage_list:
        if validate_cage(grid, i) == False:
            return False
    return True


def check_lines(grid):
    tpose = transpose(grid)
    for i in range(len(grid)):
        if validate_line(grid[i]) == False or validate_line(tpose[i]) == False:
            return False
    return True


def get_cage_list():
    cages = [input().split() for i in range(int(input()))]
    intcages = []
    for i in cages:
        cage = []
        for j in i:
            cage.append(int(j))
        intcages.append(cage)
    return intcages


def create_grid(cage_list):
    size = int((max([j for i in cage_list for j in i]) + 1) ** .5)
    grid = [[0] * size for i in range(size)]
    return grid


def grid1d_to_2d(grid):
    return [grid[i:i + int((len(grid)) ** .5)] 
            for i in range(0, len(grid), int((len(grid)) ** .5))]


def display_solution(grid):
    for i in grid:
        s = ''
        for j in i:
            if j == i[len(i) - 1]:
                s += str(j)
            else:
                s += str(j) + " "
        print(s)


def transpose(grid):
    tpose = []
    for j in range(len(grid)):
        row = []
        for i in range(len(grid)):
            row.append(grid[i][j])
        tpose.append(row)
    return tpose


def validate_line(ints):
    count = 0
    for i in ints:
        if ints.count(i) > 1 and i > 0:
            count += 1
    return count == 0


def validate_cage(grid, cage):
    flatten_list = [j for sub in grid for j in sub]
    values = [flatten_list[i] for i in cage[1:]]
    total = sum(values)
    if 0 in values:
        return total < cage[0]
    else:
        return total == cage[0]


if __name__ == "__main__":
    main()
