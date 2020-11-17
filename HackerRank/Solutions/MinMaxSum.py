#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    min_list=list(arr)
    min_list.pop(arr.index(max(arr)))
    min_sum=sum(min_list)
    max_list=list(arr)
    max_list.pop(arr.index(min(arr)))
    max_sum=sum(max_list)
    print(min_sum,max_sum)


def inputFuntion(n):
    input_list=[]
    for i in range(0,5):
        number = random.randint(0, 100)
        input_list.append(number)
    return input_list


if __name__ == '__main__':
    arr=inputFuntion(10)
    miniMaxSum(arr)
