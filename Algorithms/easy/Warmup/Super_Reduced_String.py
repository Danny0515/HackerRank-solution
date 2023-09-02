#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    charList = list(s)

    if len(charList) == 0:
        return 'Empty String'
    else:
        for i, char in enumerate(charList):
            if i + 1 < len(charList):
                if charList[i] == charList[i+1]:
                    charList.pop(i)
                    charList.pop(i)
                    newString = ''.join(charList)
                    return superReducedString(newString)
        return ''.join(charList)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
