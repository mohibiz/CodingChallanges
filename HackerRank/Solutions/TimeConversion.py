#!/bin/python3

import os
import sys
import time
import random
import datetime


#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    # format = '%I:%M %p'
    # return  datetime.datetime.strptime(s, format)
    # date_time_obj = datetime.datetime.strptime(s, '%m/%d/%Y %I:%M %p'
    h, m, s = map(int, time[:-2].split(':'))
    p = time[-2:]
    h = h % 12 + (p.upper() == 'PM') * 12
    output_str=str(('%02d:%02d:%02d') % (h, m, s))
    return output_str


def StrTimePop(start, end, format, prop):
    #Credit : Tom Alsberg
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def randomDate(start, end, prop):
    return StrTimePop(start, end, '%m/%d/%Y %I:%M:%S %p', prop)


def inputFunction():
    date_time_str=randomDate("1/1/2008 1:30:00 PM", "1/1/2020 4:50:00 AM", random.random())
    date_object = datetime.datetime.strptime(date_time_str, "%d %B, %Y")

    print(date_object)
    # return date_time_obj.time()


if __name__ == '__main__':
    s=inputFunction()
    print(f'input date is {s}')
    # result = timeConversion(s)
    # print(f'output date is {result}')
