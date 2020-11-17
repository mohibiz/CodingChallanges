#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the plusMinus function below.
def plusMinus(arr):
    positive,negative,zero=0,0,0
    for integer in arr:
        if integer>0:
            positive+=1
        elif integer<0:
            negative+=1
        else:
            zero+=1
    positive=(positive/len(arr))
    negative=(negative/len(arr))
    zero=(zero/len(arr))
    print("{:.6f}\n{:.6f}\n{:.6f}".format(positive,negative,zero));



def inputfuntion(n):
    array_list=[]
    if n>=0 and n<=100:
        for i in range(0,n):
            n=random.randint(-100, 100)
            array_list.append(n)
    return array_list


if __name__ == '__main__':
    arr=inputfuntion(10)
    plusMinus(arr)
