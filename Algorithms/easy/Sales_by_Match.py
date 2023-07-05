#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    pairsOfSocks = 0
    sockCount = {}

    for sock in ar:
        if sock not in sockCount.keys():
            sockCount[sock] = 1
        else:
            sockCount[sock] += 1

    for sockSum in sockCount.values():
        pairsOfSocks += (sockSum // 2)
    return pairsOfSocks


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
