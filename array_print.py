# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 15:57:35 2017

@author: bhupeshgupta
"""

#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

arr.reverse()
print(*arr, sep = ' ')