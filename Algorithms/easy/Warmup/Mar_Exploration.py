#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    differentCount = 0
    OCount = 1
    for i, char in enumerate(s):
        if i == OCount:
            OCount += 3
            if char != "O":
                differentCount += 1
        else:
            if char != "S":
                differentCount += 1
    return differentCount


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()