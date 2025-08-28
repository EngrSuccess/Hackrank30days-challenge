#!/bin/python3

import sys
import random
import os
import re
import math


n = int(input().strip())

binary_str = bin(n)[2:]

target_no = "1"
current_count = 0
max_count = 0

for x in binary_str:
    if x == target_no:
        current_count += 1
        if current_count>max_count:
            max_count = current_count
        else:
            max_count
    else:
        current_count = 0
print(max_count)