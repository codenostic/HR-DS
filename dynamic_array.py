# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 11:53:40 2017

@author: bhupeshgupta
"""

'''
We have - seqList which is list of N empty seq (sequences) and a variable lastAns intialize to 0 
Input - N and Q -> N gives the size of seqList, Q is number of queries on the seqList 

Each query os of type 1 x y or 2 x y 
for 1 X Y we find the seq with index ((X xor lastAns)% N) and then append Y in it
for 2 X Y we find seq ((X xor lastAns) % N ) and in that we find element at y%size(seq) 
lastAns = element then print lastAns

'''

class SeqList:    
   
   def __init__(self, N):
        '''
        given N make a list of N empty sequences
        '''
        self.array = [[] for _ in range(N)]
        self.lastAns = 0 

   def query_1(self, x,y):
        length = len(self.array)
        self.array[((x^self.lastAns)%length)].append(y)
    
   def query_2(self, x, y):
        length = len(self.array)
        seq = self.array[((x^self.lastAns)%length)]
        size = len(seq)
        element = seq[(y%size)]
        self.lastAns= element
        print(self.lastAns)
  
   def query(self, key, x, y):
         '''
         Input key, x, y 
         Output based on query 1 or query 2 
         '''
         if key == 1:
             self.query_1(x,y)
         else:
            self.query_2(x,y)


# main function starts here 
if __name__ == '__main__':
    N, Q = map(int, input().split())
    mySeqList = SeqList(N)
    for _ in range(Q):
        key, x, y = map(int, input().split())
        mySeqList.query(key, x, y)
        

'''
This implementation looks better in terms of object oriented approach. 

'''