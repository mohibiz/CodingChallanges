#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):


    if x2>x1 and v2>=v1:
        print('NO')
        return 'NO'
    elif x2<x1 and v2<v1:
        print('NO')
        return 'NO'
    else:

        while (x1<10000 or x2<=10000):
            x1 += v1
            x2 += v2
            if x1==x2:
                print('YES')
                return 'YES'
                break
        else:
            print('NO')
            return 'NO'



if __name__ == '__main__':

    # input= [x1, v1, x2, v2]
    # result = kangaroo(0,3,4,2)
    result = kangaroo(0,2,5,3)


