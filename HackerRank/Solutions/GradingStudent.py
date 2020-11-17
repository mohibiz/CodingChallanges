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
    # Write your code here
    print(grades)
    manipulated_grade=[]

    for grade in grades:
        if grade>=0 and grade<38:
            manipulated_grade.append(grade)
        elif grade>38 and grade<=100 and (math.ceil(grade/5))*5-grade>=3:
            manipulated_grade.append(grade)
        elif grade>38 and grade<=100 and (math.ceil(grade/5))*5-grade<3:
            manipulated_grade.append((math.ceil(grade/5))*5)
    return manipulated_grade



def inputFuntion(n):
    input_list = []
    for i in range(0, n):
        number = random.randint(0, 100)
        input_list.append(number)
    return input_list


if __name__ == '__main__':

    # grades_count = inputFuntion(3)

    grades = inputFuntion(1)

    result = gradingStudents([4])
    print(result)


