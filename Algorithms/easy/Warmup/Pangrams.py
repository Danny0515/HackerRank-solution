#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # [a-z] ord() --> 97-122
    pangramDitc = {ordinal: 0 for ordinal in range(97, 123)}
    for char in s.lower():
        if ord(char) in pangramDitc.keys():
            pangramDitc[ord(char)] = 1
    if sum(pangramDitc.values()) == 26:
        return 'pangram'
    else:
        return 'not pangram'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
