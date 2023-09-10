#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cavityMap' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY grid as parameter.
#

def cavityMap(grid):
    for row in range(1, len(grid) - 1):
        for column in range(1, len(grid[row]) - 1):
            center = grid[row][column]
            if center > max(grid[row - 1][column] + grid[row][column - 1] + grid[row][column + 1] + grid[row + 1][column]):
                grid[row] = grid[row][:column] + "X" + grid[row][column + 1:]
    return grid

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
