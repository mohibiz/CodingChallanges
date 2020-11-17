#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    return int(math.fsum((ar)))
        # return int(math.fsum(ar))

if __name__ == '__main__':
    ar='1000000001 1000000002 1000000003 1000000004 1000000005'

    result = aVeryBigSum(ar)
    print(result)


