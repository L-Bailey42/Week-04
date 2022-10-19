#!/usr/bin/env python3

from math import sqrt
from math import log2

WIDTH = 52

def task_1():
    print("\n")
    print(sqrt(2401))

def task_2():
    print("\n")
    print(log2(1024))

def displayTwice(msg):
    print("\n")
    print(msg)
    print(msg)

def findMax(a,b):
    print("\n")
    if (a > b):
        max = a
    else:
        max = b
    return max

def task_5(num1, num2 = num1):
    print("\n")
    result = num1*num2
    return result

def someFunc(x, y, z):
    print("\n")
    print(f"x is {x}\ny is {y}\nz is {z}")


if __name__ == "__main__":
    print(f"{'?'*WIDTH}\n{'Practice':^{WIDTH}}\n{'?'*WIDTH}")
    task_1()
    task_2()
    name = "Luke"
    displayTwice(name)
    a = 1
    b = 2
    c = 3
    print(findMax(a,b))
    task_5(a,b)
    
