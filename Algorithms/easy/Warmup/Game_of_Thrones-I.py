#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gameOfThrones' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def gameOfThrones(s):
    charCount = {}
    for char in s:
        if char in charCount.keys():
            charCount[char] += 1
        else:
            charCount[char] = 1

    palindrome = 0
    for count in charCount.values():
        if palindrome == 2:
            return "NO"
        if (count % 2 != 0) and palindrome < 2:
            palindrome += 1
    if palindrome == 2:
        return "NO"
    else:
        return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()