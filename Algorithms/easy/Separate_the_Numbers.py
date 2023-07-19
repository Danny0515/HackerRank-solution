#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    beautiful = False
    for length in range(1, len(s)//2 + 1):
        start = int(s[:length])
        tmpStr = str(start)
        while len(tmpStr) < len(s):
            start += 1
            tmpStr += str(start)
        if tmpStr == s:
            beautiful = True
            break
    if beautiful:
        print(f"YES {s[:length]}")
    else:
        print("NO")

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
