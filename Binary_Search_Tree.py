# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 17:22:32 2017

@author: bhupeshgupta
"""

'''
Binary Search Tree - 
Functions 
Insert
Delete
Search a Key 
Minimum - Recurssive, Iterative
Maximum - Recrussive, Iterative 
Successor 
Predecessor
Inorder - Recursion, Iterative
Predorder - Recursive, Iterative
PostOrder travel - Recursive, Iterative
'''

class Node(object):
    def __init__(self, data, parent = None, left = None, right = None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right 
    
def insert_node(root, key):
    new_node = Node(key)
    if root == None:
        root = new_node
    elif new_node.data < root.data:
        if root.left == None:
            root.left = new_node
            new_node.parent = root
        else:
            root.left = insert_node(root.left, key)
    else:
        if root.right == None:
            root.right = new_node
            new_node.parent = root
        else:
            root.right = insert_node(root.right, key)
            
    return root


def binary_delete(root, data):
    '''
    Input - Root Node and Data to be deleted 
    Output - Give back new root and True if removed else same root and false
    '''
    # Base Case
    if root is None:
        return root 
 
    # If the key to be deleted is smaller than the root's
    # key then it lies in  left subtree
    if data < root.data:
        root.left = binary_delete(root.left, data)
 
    # If the kye to be delete is greater than the root's key
    # then it lies in right subtree
    elif(data > root.data):
        root.right = binary_delete(root.right, data)
 
    # If key is same as root's key, then this is the node
    # to be deleted
    else:
        if root.left == None and root.right == None:
            root = None
         
        # Node with only one child or no child
        elif root.left is None :
            temp = root.right
            temp.parent = root.parent
            root = None 
            return temp
        elif root.right is None :
            temp = root.left
            temp.parent = root.parent 
            root = None
            return temp
                        
        else:
        # Node with two children: Get the inorder successor
        # (smallest in the right subtree)
            temp = imin_tree(root.right).data
 
            # Copy the inorder successor's content to this node
            root.data = temp
 
        # Delete the inorder successor
            root.right = binary_delete(root.right , temp)
 
 
    return root    

def rmin_tree(root):
    if root.left is None:
        return root
    else:
        return rmin_tree(root.left)
        
def imin_tree(root):
    while root.left is not None:
        root = root.left
    return root

def rmax_tree(root):
    if root.right is None:
        return root
    else:
        return rmax_tree(root.right)

def imax_tree(root):
    while root.right is not None:
        root = root.right
    return root

def find_node(root, data):
    if root == None:
        return None
    elif root.data == data:
        return root
    elif data > root.data:
        return find_node(root.right, data)
    elif data< root.data:
        return find_node(root.left, data)
    else: 
        return None

def node_successor(node):
    if node.right is not None:
        return imin_tree(node.right)
    else:
        ancestor = node.parent
        while ancestor != None and node != ancestor.left:
            node = ancestor
            ancestor = ancestor.parent
        return ancestor

def node_pred(node):
    if node.left is not None:
        return imax_tree(node.left)
    else:
        ancestor = node.parent
        while ancestor != None and node != ancestor.right:
            node = ancestor 
            ancestor = ancestor.parent
        return ancestor 

def print_node(node):
    print(node.data)
    
def inorder(root):
    l = []
    if root == None:
        return []
    else:
        l += inorder(root.left)
        l.append(root.data)
        l += inorder(root.right)
    return l
    
def inorder_i(root):
    pass

def preorder(root):
    l = []
    if root == None:
        return []
    else:
        l.append(root.data)
        l += preorder(root.left)
        l += preorder(root.right)
    return l

def postorder(root):
    l = []
    if root == None:
        return []
    else:
        l += postorder(root.left)
        l += postorder(root.right)
        l.append(root.data)
    return l


