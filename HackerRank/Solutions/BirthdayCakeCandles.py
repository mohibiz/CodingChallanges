#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    # print(candles)
    tallest_candle=max(candles)
    print(candles.count(tallest_candle))


def inputFuntion(n):

    input_list = []
    for i in range(0, n):
        number = random.randint(1, pow(10,5))
        input_list.append(number)
    return input_list


if __name__ == '__main__':
    candles=inputFuntion(4)
    result = birthdayCakeCandles(candles)

