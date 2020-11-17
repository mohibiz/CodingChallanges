#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    x,y=0,0
    if len(a)==len(b):
        for i in range(0,len(a)):
            if a[i]>b[i]:
                x=x+1
            elif a[i]<b[i]:
                y=y+1
            else:
                x=x+0
                y=y+0
    else:
        print('invalid comparison as lengths of input is not same')
    return [x,y]

if __name__ == '__main__':

    a=[1,2,3]
    b=[2,2,2]
    result = compareTriplets(a, b)
    # print(result)

