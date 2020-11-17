#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    max_base_score=min_base_score=scores[0]
    max_score_count=min_score_count=0

    for index , score in enumerate(scores):
        if index>0 and score>max_base_score:
            max_base_score=score
            max_score_count+=1

        if index > 0 and score < min_base_score:
            min_base_score = score
            min_score_count += 1
    print(max_score_count,min_score_count)

    return max_score_count,min_score_count



if __name__ == '__main__':
    # scores=[10, 5, 20, 20, 4 ,5, 2, 25, 1]
    scores=[3, 4, 21, 36, 10, 28, 35, 5, 24, 42]

    result = breakingRecords(scores)

