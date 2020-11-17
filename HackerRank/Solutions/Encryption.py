#!/bin/python3

import math
import os
import random
import re
import sys
import string


# Complete the encryption function below.
def encryption(s):
        s=s.strip(string.whitespace)
        encoded_string =''
        encoded_list=[]
        L=math.sqrt(len(s))
        print(f'length of string is {L}')
        no_of_row=math.floor(L)
        no_of_column=math.ceil(L)
        print(no_of_row,no_of_column)
        for i,letter in enumerate(s):
            encoded_string+=letter
            if (i+no_of_column+1)%no_of_column==0:
                # print(encoded_string)
                encoded_list.append(encoded_string)
                encoded_string=''
        e_string = ''
        for str in encoded_list:
            for letter in str :
                print(letter)


        # print(tuple(encoded_list))
            # encoded_string='#'.join(encoded_string)
    # print(encoded_string)
    # print(s.split(no_of_column,'\n',no_of_row))


def inputFuntion(chars,size):
    res = []
    s=random_string_generator(size, chars)
    for letters in s:
        res.append(letters.replace("\n", ""))
    return ''.join(res)


def random_string_generator(str_size, allowed_chars):
    return ''.join(random.choice(allowed_chars) for x in range(str_size))


if __name__ == '__main__':
    s=inputFuntion(string.ascii_lowercase + string.whitespace + string.ascii_uppercase,12)
    print(f'orignal string is {s}')
    result = encryption('haveaniceday')

