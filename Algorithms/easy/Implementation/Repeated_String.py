#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(repeated_string, number):
    if repeated_string == "a":
        return number

    total = 0
    a_in_repeated_string = 0
    for letter in repeated_string:
        if letter == "a":
            a_in_repeated_string += 1

    repeated_times = number // len(repeated_string)
    last_letter_count = number % len(repeated_string)
    for i in range(last_letter_count):
        if repeated_string[i] == "a":
            total += 1
    return total + (a_in_repeated_string * repeated_times)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
