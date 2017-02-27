# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 14:38:57 2017

@author: bhupeshgupta
"""

'''
left rotations - Objective: perform d left rotations for and array of size n
one left rotation means last element moved to index 0 and elements 0 to n-2 shifted to right by 1

'''




# main function starts here 
if __name__ == '__main__':
    n, d = map(int, input().split())
    array = [int(x) for x in input().split()]

    array = array[d:] + array[0:d]
    print(*array, sep = ' ')

'''
this is optimized code but did not use objects which is fine as this is done better this way. 
'''
