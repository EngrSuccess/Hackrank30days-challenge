#!/bin/python3

import math
import os
import random
import re
import sys

def compare():
    n = int(input().strip())
    if n % 2 == 1:
        print('Weird')
    elif n % 2 == 0 and n < 5:
        print('Not Weird')
    elif n % 2 == 0 and n > 0 and n > 5 and n <= 20:
        print('Weird') 
    elif n % 2 == 0 and n > 20:
        print('Not Weird')
    else:
        print('Invalid')




if __name__ == '__main__':
    compare()
    