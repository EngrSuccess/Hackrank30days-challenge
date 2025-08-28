#!/bin/python3

import os
import math
import re
import random
import sys

n = int(input())

myList = list(map(int, input().rstrip().split()))

myList.reverse()

print(*myList)