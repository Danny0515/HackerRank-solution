#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    ans = []
    for grade in grades:
        roundGrade = 5 * (grade // 5 + 1)
        if (grade % 5 >= 3) and (roundGrade >= 40):
            ans.append(roundGrade)
        else:
            ans.append(grade)
    return ans


if __name__ == '__main__':

    grades = [73, 67, 38, 33]

    result = gradingStudents(grades)
    print(result)
    #
    # print(70 % 5)
    # print(71 % 5)
    # print(72 % 5)
    # print(73 % 5)
    # print(74 % 5)
    # print('------')
    # print(70 // 5)
    # print(71 // 5)
    # print(72 // 5)
    # print(73 // 5)
    # print(74 // 5)
