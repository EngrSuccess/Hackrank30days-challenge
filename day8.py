#!/bin/python3

x = int(input())
dic = {}

for i in range(x):
    a = input().split(' ', 1)
    dic[a[0]] = a[1]

try: 
    while True:
        a = input()
        if len(a) > 0:
            if a in dic:
                print(f'{a}={dic[a]}')
            else:
                print('Not found')
except EOFError:
    pass