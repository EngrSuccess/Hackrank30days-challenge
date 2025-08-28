#!/bin/python3

# Recurrsion


def summation(n):
    # n = int(input())
    if n <= 0: # Base case
        return n
    else:
        return n + summation(n - 1) #Recurssion case
    

def factorial(n):
    # n = int(input())
    if n <= 1:
        return 1 # Base case
    else:
        return n * factorial(n - 1) #Recurssion Case
    
def exponention(n, p):
    # p - Number of times to be multiplied
    # n - The number to multiply
    if p <= 0:
        return 1
    else:
        return n * exponention(n, p - 1)


if __name__ == "__main__":
    print(summation(3))
    print(factorial(3))
    print(exponention(3, 3))