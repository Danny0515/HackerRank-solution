#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#

def beautifulDays(i, j, k):
    days = [day for day in range(i, j + 1)]
    beautiful = 0

    for day in days:
        reversedDay = int(''.join(reversed([char for char in str(day)])))
        if abs(reversedDay - day) % k == 0:
            beautiful += 1
    return beautiful


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
