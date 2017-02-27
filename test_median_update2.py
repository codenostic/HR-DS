# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 11:28:17 2017

@author: bhupeshgupta
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 09:56:34 2017

@author: bhupeshgupta
"""

'''
Median Update 
'''
#!/bin/python

class Node(object):
    def __init__(self, val, left = None, right = None):
        self.data = val
        self.left = left
        self.right = right

def binary_insert(root, data):
    '''
    Input - Root Node and Data
    Output - Give back new Root
    '''
    new_node = Node(data)
    
    if root == None:
        root = new_node
    elif new_node.data > root.data:
        if root.right == None:
            root.right = new_node
        else:
            binary_insert(root.right, data)
    else:
        if root.left == None:
            root.left = new_node
        else:
            binary_insert(root.left, data)
    
    return root

def find_min(root):
    if root.left != None:
        return find_min(root.left)
    else:
        return root.data

def binary_delete(root, data):
    '''
    Input - Root Node and Data to be deleted 
    Output - Give back new root and True if removed else same root and false
    '''
    # if node is None just return dont do anything
    if root == None:
        return None
    elif data > root.data:
        return binary_delete(root.right, data)
    elif data < root.data:
        return binary_delete(root.left, data)
    elif root.data == data:
   # if node - left and right both none just remove node and return None 
        if root.left == None and root.right == None:
            return None
    # if node has one child either left or right then return child 
        elif root.left is None and root.right is not None:
            return root.right
        elif root.left is not None and root.right is None:
            return root.left            
    # if node has both right and left child then find min from right child, replace with min, remove min and return new
        else:
            root.data = find_min(root.right)
            binary_delete(root.right, root.data)
            return root
# Given a binary search tree and a key, this function
# delete the key and returns the new root
def deleteNode(root, key):
 
    # Base Case
    if root is None:
        return root 
 
    # If the key to be deleted is similiar than the root's
    # key then it lies in  left subtree
    if key < root.data:
        root.left = deleteNode(root.left, key)
 
    # If the kye to be delete is greater than the root's key
    # then it lies in right subtree
    elif(key > root.data):
        root.right = deleteNode(root.right, key)
 
    # If key is same as root's key, then this is the node
    # to be deleted
    else:
         
        # Node with only one child or no child
        if root.left is None :
            temp = root.right 
            root = None
            return temp 
             
        elif root.right is None :
            temp = root.left 
            root = None
            return temp
 
        # Node with two children: Get the inorder successor
        # (smallest in the right subtree)
        temp = find_min(root.right)
 
        # Copy the inorder successor's content to this node
        root.data = temp
 
        # Delete the inorder successor
        root.right = deleteNode(root.right , temp)
 
 
    return root 
    
def inorder_list(root):
    '''
    Input - Root Node
    Output - List using inorder traversal
    '''
    cur_list = []
    if root == None:
        return []
    else:
        cur_list += inorder_list(root.left)
        cur_list.append(root.data)
        cur_list += inorder_list(root.right)

    return cur_list
    
def inorder_print(root):
    if root == None:
        return 
    inorder_print(root.left)
    print(root.data)
    inorder_print(root.right)
        

def find_median(cur_list, list_sz):
    '''
    Input - List, Size 
    OutPut - median
    '''
    if list_sz == 1:
        return cur_list[0]
    elif list_sz == 2:
        return (sum(cur_list)/2)
    else:
        if list_sz%2 == 0:
            med_ind = list_sz//2
            median = (cur_list[med_ind-1] + cur_list[med_ind])/2
            return median
        else:
            med_ind = list_sz //2 
            median = cur_list[med_ind]
            return median

def median(a,x):
    cur_root = None 
    list_sz = 0
    cur_list = []
    while a: 
        key = a.pop(0)
        new_int = x.pop(0)
        # if add then add a node and get root. 
        if key == 'a':
            cur_root = binary_insert(cur_root, new_int)
            list_sz += 1
        # then get median
            cur_list.clear()
            cur_list = inorder_list(cur_root)
#            print(cur_list)
#            inorder_print(cur_root)
            median = str(find_median(cur_list, list_sz))
            print(median.rstrip('0').rstrip('.') if '.' in median else median)
                           
        # if remove and size > 0 and it is present in list then remove. 
        elif key =='r':
            if list_sz > 0:
                if new_int in cur_list:
                    cur_root = deleteNode(cur_root, new_int)
                    list_sz -=1
                    cur_list.clear()
                    cur_list = inorder_list(cur_root)
#                    print(cur_list)
#                    inorder_print(cur_root)
                    if list_sz > 0:
                        median = str(find_median(cur_list, list_sz))
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
s = [] # maintain a list of A or R
x = [] # maintain corresponding interger 
for i in range(0, N):
   tmp = input().strip().split(' ')
   a, b = [xx for xx in tmp]
   s.append(a)
   x.append(int(b))
median(s,x)