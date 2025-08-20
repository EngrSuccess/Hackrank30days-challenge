#!/bin/python3

import math
import os
import sys
import re
import random

def multipLoop():
    n = int(input().strip())
    y = 0
    while y < 10:
        y += 1
        print(f"{n} x {y} = {n * y}")
        


if __name__ == "__main__":
    multipLoop()