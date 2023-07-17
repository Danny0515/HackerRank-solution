#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    digit = False
    lowercase = False
    uppercase = False
    specialCharacter = False

    for char in password:
        # 48-57 [0-9]
        if 48 <= ord(char) <= 57:
            digit = True
        # 65-90 [A-Z]
        if 65 <= ord(char) <= 90:
            uppercase = True
        # 97-122 [a-z]
        if 97 <= ord(char) <= 122:
            lowercase = True
        if char in '!@#$%^&*()-+':
            specialCharacter = True

    requiredCondition = 4 - digit - lowercase - uppercase - specialCharacter
    newPwdLength = len(password) + requiredCondition

    if newPwdLength >= 6:
        return requiredCondition
    else:
        return requiredCondition + (6 - len(password) - requiredCondition)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
