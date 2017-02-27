# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 14:43:44 2017

@author: bhupeshgupta
"""

'''
optimize Valid_C3C2 

'''

import operator
import time

def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print ('%s function took %0.3f ms' % (f.__name__ , (time2-time1)*1000.0))
        return ret
    return wrap
    
#@timing    
def valid_Cw_list(possible_C3C2):
    # if no entry in possible_C3C2 then just return -1
    if len(possible_C3C2) == 0 :
        return -1
    
    valid_C3 = [] # if we have valid C3 the we save C2 trees in this for validation
    valid_C3C2 = [] # save if we get C2 also valid with Cw so that we can give out Cw
    while possible_C3C2:
        # pop means we start from highest C3 that means Lowest Cw
        item = possible_C3C2.pop()
        C2_item, C3_item = item['C2'], item['C3']
        C2, C2_trees_list = C2_item
        C3, C3_trees_list = C3_item
        print(C2_trees_list, 'C2_trees', C3_trees_list, 'C3_trees')
        # here we make sure that for a given C3 there is are 2 ValidC2's 
        for tree in C3_trees_list:
            valid = [ 0 if len(set(item)-(set(item)-set(tree))) > 0 else 1 for item in C2_trees_list]
            if sum(valid) >= 2:
                valid_C3.append(((C2-C3),C2_trees_list))
                break
            else:
                continue
        print(valid_C3, 'Valid_C3')
        
        for Cw, C2_trees_list in valid_C3:

            temp_C2_trees = C2_trees_list[:]
            print(C2_trees_list, 'again print C2_trees', temp_C2_trees, 'temp_c2')
            for tree in C2_trees_list:
                valid = [ 0 if len(set(item)-(set(item)-set(tree))) > 0 else 1 for item in temp_C2_trees]
                print(valid, 'valid_c3c2')
                if sum(valid) >= 1:
                    valid_C3C2.append((Cw, [item, tree]))
                    break
    print(valid_C3C2, 'Valid_C3C2')
    if len(valid_C3C2) > 0:            
        return min(valid_C3C2, key = operator.itemgetter(0))[0]
    else:
        return -1
        


#test cases Inputs  - Possible C3C2's 
possible_6_1 = []

possible_8_1 = \
[{'C3': (1, [(3,), (1,), (2,)]), 'C2': (26, [(5, 6, 7), (8, 4, 2, 1)])}, \
{'C3': (3, [(3, 2, 1)]), 'C2': (25, [(6, 7, 8, 3, 2, 1), (8, 4, 1)])}, \
{'C3': (5, [(7,)]), 'C2': (24, [(6, 7, 8, 2, 1), (5, 7, 8, 3, 2, 1)])}, \
{'C3': (7, [(8, 1)]), 'C2': (23, [(5, 7, 8, 2, 1), (6, 7, 8, 1)])}, \
{'C3': (9, [(8, 3, 2, 1)]), 'C2': (22, [(5, 7, 8, 1), (6, 7, 8)])}, \
{'C3': (11, [(7, 8), (6,)]), 'C2': (21, [(5, 7, 8), (4, 3, 2, 1)])}]


possible_6_2 = [{'C3': (17, [(4,)]), 'C2': (30, [(3, 2, 1), (6, 5)])}]

possible_8_2 = [{'C3': (10, [(1,), (8, 7), (6, 5)]), 'C2': (15, [(7, 6, 5), (6, 5, 4), (4, 1), (3, 2, 1)])}]

possible_6_3 = [{'C3': (0, [()]), 'C2': (297, [(5, 3, 1), (6, 4, 2)])}]

possible_14_1 = \
[{'C3': (6, [(8,)]), 'C2': (62, [(6, 7, 8, 4, 10, 9, 3, 2, 1), (7, 8, 4, 11, 10, 9, 3, 2, 1), (14, 13, 12, 9, 3, 2, 1)])}, \
{'C3': (8, [(8, 2, 1)]), 'C2': (61, [(7, 8, 12, 11, 10, 9, 3, 2, 1), (14, 13, 12, 9, 3, 2), (7, 8, 4, 12, 9, 3, 2, 1), (6, 7, 8, 12, 10, 9, 3, 2, 1), (5, 7, 8, 4, 10, 9, 3, 2, 1)])}, \
{'C3': (10, [(14,), (5,)]), 'C2': (60, [(14, 13, 12, 9, 3), (5, 7, 8, 12, 10, 9, 3, 2, 1)])}, \
{'C3': (12, [(9,), (7, 8, 1)]), 'C2': (59, [(13, 12, 10, 9, 3, 2, 1), (14, 13, 12, 9)])},\
{'C3': (14, [(9, 3, 2), (7, 8, 3, 2, 1)]), 'C2': (58, [(8, 13, 12, 9, 3, 2, 1), (13, 12, 10, 9, 3, 2)])},\
{'C3': (16, [(6, 7)]), 'C2': (57, [(13, 12, 10, 9, 3), (8, 4, 11, 10, 9, 3, 2, 1), (4, 12, 10, 9, 3, 2, 1)])},\
{'C3': (18, [(4,), (11, 10)]), 'C2': (56, [(8, 4, 12, 9, 3, 2, 1), (8, 12, 11, 10, 9, 3, 2, 1), (13, 12, 10, 9)])}, \
{'C3': (20, [(10, 9, 3), (4, 2, 1), (13,)]), 'C2': (55, [(6, 7, 8, 4, 9, 3, 2, 1), (6, 7, 8, 11, 10, 9, 3, 2, 1)])},\
{'C3': (22, [(5, 7, 8, 1), (6, 7, 8), (10, 9, 3, 2, 1)]), 'C2': (54, [(6, 7, 8, 12, 9, 3, 2, 1), (5, 7, 8, 11, 10, 9, 3, 2, 1), (5, 6, 7, 8, 10, 9, 3, 2, 1), (5, 7, 8, 4, 9, 3, 2, 1)])}, \
{'C3': (24, [(5, 7, 8, 3, 2, 1), (6, 7, 8, 2, 1)]), 'C2': (53, [(5, 7, 8, 12, 9, 3, 2, 1), (5, 6, 7, 8, 4, 3, 2, 1)])}, \
{'C3': (26, [(7, 8, 9, 3, 2, 1), (8, 4, 2, 1), (5, 6, 7)]), 'C2': (52, [(13, 12, 9, 3, 2, 1), (5, 6, 7, 8, 4, 2, 1)])}, \
{'C3': (28, [(8, 10, 9, 3, 2, 1)]), 'C2': (51, [(5, 6, 7, 8, 4, 1), (4, 11, 10, 9, 3, 2, 1), (7, 8, 4, 10, 9, 3, 2, 1), (13, 12, 9, 3, 2)])}, \
{'C3': (30, [(11, 10, 9), (12, 9, 3), (7, 8, 4, 1), (14, 13)]), 'C2': (50, [(4, 12, 9, 3, 2, 1), (12, 11, 10, 9, 3, 2, 1), (7, 8, 12, 10, 9, 3, 2, 1), (13, 12, 9, 3)])}, \
{'C3': (32, [(11, 10, 9, 3, 2), (5, 6, 7, 8), (12, 9, 3, 2, 1), (7, 8, 4, 3, 2, 1)]), 'C2': (49, [(13, 12, 9), (12, 11, 10, 9, 3, 2)])}, \
{'C3': (36, [(12, 10, 9), (5, 7, 8, 9, 3, 2, 1)]), 'C2': (47, [(12, 11, 10, 9), (14, 13, 12), (5, 6, 7, 8, 9, 3, 2, 1)])}, \
{'C3': (42, [(6, 7, 8, 4, 2, 1), (5, 7, 8, 4, 3, 2, 1)]), 'C2': (44, [(7, 8, 11, 10, 9, 3, 2, 1), (6, 7, 8, 10, 9, 3, 2, 1), (7, 8, 4, 9, 3, 2, 1)])}]

# output for each input 
#print(valid_Cw_list(possible_6_1))
#print(valid_Cw_list(possible_8_1))
#print(valid_Cw_list(possible_6_2))
#print(valid_Cw_list(possible_8_2))
#print(valid_Cw_list(possible_6_3))
print(valid_Cw_list(possible_14_1))
