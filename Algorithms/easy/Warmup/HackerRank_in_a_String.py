#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'hackerrankInString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
def hackerrankInString(s):
    target = 'hackerrank'
    result = 0
    subCharIndex = 0

    for char in target:
        for i in range(subCharIndex, len(s)):
            if char == s[i]:
                result += 1
                subCharIndex = i + 1
                break
    if result == len(target):
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
