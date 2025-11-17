#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    A = sorted(keyboards)
    B = sorted(drives)
    i = 0
    j = len(B) - 1
    best = -1

    while i < len(A) and j >= 0:
        s = A[i] + B[j]
        if s < b:
            if best is None or s > best:
                best = s
            i += 1
        else:
            j -= 1

    return best

if __name__ == '__main__':
    sys.stdout = sys.__stdout__

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    sys.stdout.write(str(moneySpent) + '\n')

    sys.stdout.close()
