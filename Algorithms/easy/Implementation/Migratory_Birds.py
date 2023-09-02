#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    birdsCount = {}
    for bird in arr:
        if bird not in birdsCount.keys():
            birdsCount[bird] = 0
        else:
            birdsCount[bird] += 1
    minTypes = {bird: count for bird, count in birdsCount.items() if count == max(birdsCount.values())}
    return min(minTypes.keys())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
