#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    origin = [ord(char) for char in s]
    reverse = [ord(char) for char in reversed(s)]
    originDifference = [abs(origin[i] - origin[i + 1]) for i in range(0, len(origin) - 1)]
    reverseDifference = [abs(reverse[i] - reverse[i + 1]) for i in range(0, len(reverse) - 1)]
    if originDifference == reverseDifference:
        return "Funny"
    return "Not Funny"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
