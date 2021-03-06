#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    magDict = {}
    noteDict = {}

    for word in magazine:
        if word not in magDict.keys():
            magDict[word] = 1
        else:
            # print(magDict)
            magDict[word] += 1
    for word in note:
        if word not in noteDict.keys():
            noteDict[word] = 1
        else:
            noteDict[word] += 1
    for word in noteDict.keys():
        if (word not in magDict.keys()) or (magDict[word] - noteDict[word] < 0):
            print('No')
            return
    print('Yes')


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
