#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gemstones' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY arr as parameter.
#

def gemstones(arr):
    gemstones = 0
    # [a-z] 97-122
    for i in range(97, 123):
        lowercaseLetter = chr(i)
        tmpCount = 0
        for array in arr:
            if lowercaseLetter in array:
                tmpCount += 1
        if tmpCount == len(arr):
            gemstones += 1
    return gemstones

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
