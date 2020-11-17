#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for stairs in range(1, n + 1):
        print(' ' * (n - stairs) + '#' * stairs)


def inputFuntion(n):
    return n


if __name__ == '__main__':
    staircase(6)
