# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 10:09:03 2017

@author: bhupeshgupta
"""

'''
here what we are trying is that we are using Counter container for storing data. 
This will help because we have lot of entries with equivalent value

'''
import collections 
import time

def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print ('%s function took %0.3f ms' % (f.__name__ , (time2-time1)*1000.0))
        return ret
    return wrap
    
#!/bin/python
def insert_data(data):
    if data in item_counter.keys():
        item_counter[data] += 1
    else:
        item_counter[data] = 1

def delete_data(data):
    if item_counter[data] > 1:
        item_counter[data] -= 1
    else:
        item_counter.pop(data)

def item_atindex(index):
    for key in sorted(item_counter):
        if (index - item_counter[key]) > 0:
            index = index - item_counter[key]
        else:
            return key
            
def cur_median(list_sz):
    if list_sz == 0:
        return 'Wrong!'
    elif list_sz == 1:
        return list(item_counter.keys())[0]
    else:
        if list_sz%2 == 0:
            med_index = list_sz//2
#            print(item_atindex(med_index) , item_atindex(med_index+1))            
            median = (item_atindex(med_index) + item_atindex(med_index+1))/2
            
            return median
        else:
            med_index = list_sz//2
#            print(item_atindex(med_index+1))
            median = item_atindex(med_index+1)
            return median 

@timing
def median(a,x):
    global item_counter
    list_sz = 0 
    item_counter = collections.Counter()
    while a:
        key = a.pop(0)
        data = x.pop(0)
        if key == 'a':
            insert_data(data)
            list_sz += 1
#            print(item_counter, list_sz)
            median = str(cur_median(list_sz))
            print(median.rstrip('0').rstrip('.') if '.' in median else median)
        elif key == 'r':
            if list_sz > 0:
                if item_counter[data]:
                    delete_data(data)
                    list_sz -= 1
#                    print(item_counter, list_sz)
                    if list_sz > 0:
                        median = str(cur_median(list_sz))
                        print(median.rstrip('0').rstrip('.') if '.' in median else median)
                    else:
                        print('Wrong!')
                        continue
                else:
                    print('Wrong!')
                    continue
            else:
                print('Wrong!')
                continue 

    
# inputs 
N = int(input())
s = []
x = []
for i in range(0, N):
   tmp = input().strip().split(' ')
   a, b = [xx for xx in tmp]
   s.append(a)
   x.append(int(b))
median(s,x)
