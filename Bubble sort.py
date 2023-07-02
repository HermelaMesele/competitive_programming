#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#import sys

n = int(input())                # Taking the number of elements in array from user .
a = [int(i) for i in input().strip().split(' ')]    # Taking the elements from user .
numSwaps = 0                #Intializing numSwaps to zero.

for i in range(n):      
    current_Swaps = 0   

    for j in range(0, n - 1):  
        if a[j] > a[j + 1]:   # Swap if the first element is greater than second
            a[j], a[j + 1] = a[j + 1], a[j]  
            current_Swaps += 1
            numSwaps += 1

    if current_Swaps == 0:
        break

print("Array is sorted in " + str(numSwaps) + " swaps.")
print("First Element: " + str(a[0]))
print("Last Element: " + str(a[n - 1]))
