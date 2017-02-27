# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 16:30:43 2017

@author: bhupeshgupta
"""
'''
given an array of size 6x6, find highest sum of 16 hour glass in the array. 
example 

INPUT
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

OUTPUT
7

INPUT 
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

OUTPUT
19

I would like to implement this in object oriented approach. SO let see what all we need. 
basically we need to create an object hourglass. 
1) An hourglass object will have input as array of 6x6 

What Methods we need 
1) max_hourglass(self) - gives back max sum out of all 16 hourglass sums 
2) sum_index(hourglass, centre_index) - given a valid index for centre element, give back sum
3) method first_sum


'''

class Hourglass:
    def __init__(self, array):
        self.array = array
    
    def first_sum(self):
        return self.array[1-1][1-1] + self.array[1-1][1] + self.array[1-1][1+1]\
                + self.array[1][1] + self.array[1+1][1-1] + self.array[1+1][1] + self.array[1+1][1+1]

    def sum_index(self, i, j):
        return self.array[i-1][j-1] + self.array[i-1][j] + self.array[i-1][j+1]\
                + self.array[i][j] + self.array[i+1][j-1] + self.array[i+1][j] + self.array[i+1][j+1]
                
    def max_hourglass(self):
        max_hourglass = self.first_sum()
        for i in range(1,5):
            for j in range(1,5):
                sum_ij = self.sum_index(i, j)
                if sum_ij > max_hourglass:
                    max_hourglass = sum_ij
        return max_hourglass

    
#!/bin/python3

import sys


arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)
hg1 = Hourglass(arr)
print(hg1.max_hourglass())


'''
i wanted to solve using object oriented approach. which i did but the code is very clumsy. 
Clumsy because 
1) application of object oriented approach is notdone well - intialazation as well as methods
2) even the negative case is handled in a clumsy manner 

lets first solve the negative case first. 
so basically what should we do if sumij < 0. lets initialize it to teh first hourglass sum. 

Got it this looks much better now. still not happy with initialization\
but atleast i solved the other 2 problems i.e. code looks clean and negative values
 lets move on to next problem 
'''
