#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    result = 1
    a.sort()
    digitCount = {}

    for digit in a:
        if digit in digitCount.keys():
            digitCount[digit] += 1
        else:
            digitCount[digit] = 1
    digits = [key for key in digitCount.keys()]

    for i, digit in enumerate(digits):
        try:
            if abs(digit - digits[i + 1]) <= 1:
                totalLen = digitCount[digit] + digitCount[digit + 1]
                if (totalLen > result):
                    result = totalLen
        except IndexError:
            break
    if result > max(digitCount.values()):
        return result
    else:
        return max(digitCount.values())


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
