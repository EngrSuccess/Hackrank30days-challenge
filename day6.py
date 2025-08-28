#!/bin/python3


# Objective
# Today we will expand our knowledge of strings, combining it with what we have already learned about loops. Check out the Tutorial tab for learning materials and an instructional video.

# Task
# Given a string, , of length  that is indexed from  to , print its even-indexed and odd-indexed characters as  space-separated strings on a single line (see the Sample below for more detail).

# Note:  is considered to be an even index.

# Example


# Print abc def
num = int(input())

for i in range(num):
    s = input()
    even_string = s[::2]
    odd_string = s[1::2]

    print(f"{even_string} {odd_string}") 

