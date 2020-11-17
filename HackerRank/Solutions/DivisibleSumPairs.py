#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    k_divisible_count=0
    for i,a in enumerate(ar):
        for j,b in enumerate(ar):
            if i<j and ((a+b)%k)==0:
                k_divisible_count+=1
    print(k_divisible_count)


if __name__ == '__main__':

    ar= [1, 3, 2, 6, 1, 2]
    result = divisibleSumPairs(6, 3, ar)


