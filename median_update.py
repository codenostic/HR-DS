# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 14:10:03 2017

@author: bhupeshgupta
"""

'''
Median Updates
'''

#!/bin/python

class Node:
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.data = val

def binary_insert(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.l_child is None:
                root.l_child = node
            else:
                binary_insert(root.l_child, node)
        else:
            if root.r_child is None:
                root.r_child = node
            else:
                binary_insert(root.r_child, node)

def in_order_print(root):
    if not root:
        return
    in_order_print(root.l_child)
    print (root.data)
    in_order_print(root.r_child)      



def median(a,x):
    # lets have two global variables cur_list, list_size
    global cur_list, list_sz
    cur_list = []
    list_sz = 0
    # while a and x we keep going 
    while a:
        key = a.pop(0)
        new_node = Node(x.pop(0))
#        print(key, new_int, a, x)
    # if a then add and give median 
        if key == 'a':
            if list_sz == 0:
                root = None
                binary_insert(root, new_node)
            else:
                add(new_int, 0, list_sz-1)
            list_sz += 1
            if list_sz > 1:
                if list_sz%2 == 0:
                    median_index = list_sz//2
                    median = (cur_list[median_index-1] + cur_list[median_index])/2
                    m = str(median)
                    print(m.rstrip('0').rstrip('.') if '.' in m else m)
                else:
                    median_index = list_sz//2 +1
                    median = cur_list[median_index-1]
                    print(median)
            else:
                median = cur_list[0]
                print(median)
    # if remove and list size > 0 then remove and print median 
        elif key == 'r':
            removed = remove(new_int)
            if removed:
                list_sz -= 1
                if list_sz > 0:
                    if list_sz%2 == 0:
                        median_index = list_sz//2
                        median = (cur_list[median_index-1] + cur_list[median_index])/2
                        m = str(median)
                        print(m.rstrip('0').rstrip('.') if '.' in m else m)
                    else:
                        median_index = list_sz//2 +1
                        median = cur_list[median_index-1]
                        print(median)
                else:
                    print('Wrong!')
            else:
                print('Wrong!')

    
#input 
N = int(input())
s = []
x = []
for i in range(0, N):
   tmp = input().strip().split(' ')
   a, b = [xx for xx in tmp]
   s.append(a)
   x.append(int(b))
median(s,x)
