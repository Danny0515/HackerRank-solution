#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    ans = []
    for i in range(4):
        for k in range(4):
            tmpArr = []
            tmpArr.append(arr[i][k])
            tmpArr.append(arr[i][k + 1])
            tmpArr.append(arr[i][k + 2])
            tmpArr.append(arr[i + 1][k + 1])
            tmpArr.append(arr[i + 2][k])
            tmpArr.append(arr[i + 2][k + 1])
            tmpArr.append(arr[i + 2][k + 2])
            ans.append(sum(tmpArr))
    return(max(ans))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
