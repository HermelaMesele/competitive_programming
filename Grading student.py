#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
n = int(input().strip())
for a0 in range(n):
    grade = int(input().strip())

    if grade >= 38:
        mod5 = grade % 5
        if mod5 >= 3:
            grade = grade + (5 - mod5)
    print(grade)
