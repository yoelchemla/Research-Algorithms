import sys
import math


def next_grow(n):
    t = n + 1
    while not temp(t):
        t += 1
    return t


def temp(t):
    res = [(x) for x in str(t)]

    for j in range(len(res)-1):
        if res[j] > res[j + 1]:
            return False
    return True


if __name__ == '__main__':
    print(next_grow(19))
# 99 -> 111
