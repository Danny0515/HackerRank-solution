#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    first_like_people = 5 // 2
    last_day_like = None
    cumulative = 0

    for _ in range(n):
        if not last_day_like:
            last_day_like = first_like_people
            cumulative += last_day_like
            continue
        today_like_people = last_day_like * 3 // 2
        last_day_like = today_like_people
        cumulative += today_like_people
    return cumulative

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
