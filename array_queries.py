# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 20:52:26 2017

@author: bhupeshgupta
"""

'''
Array and Queries 

'''


# inputs 
N,M = map(int, input().split())
A = list(map(int, input().split()))
X = [x for x in range(N)]
for _ in range(M):
    flag,i,j = map(int, input().split())
    X = (X[i-1:j] + X[:i-1] + X[j:]) if flag == 1 else  (X[:i-1] + X[j:] + X[i-1:j])
A = [A[x] for x in X]
print(abs(A[0]-A[-1]))
print(*A)
