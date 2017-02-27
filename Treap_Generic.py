# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 09:09:08 2017

@author: bhupeshgupta
"""

'''
Treap
Structure and Methods 
insert, delete, find, inorder traversal, right rotation, left rotation
Split, Merge 
'''
import random

class Node(object):
    def __init__(self, data, left = None, right = None, parent = None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        self.priority = random.random()
        self.size = 1

def insert(root, node):
    if root == None:
        root = node
    elif node.data < root.data:
        if root.left == None:
            root.left = node
            root.left.parent = root
            root.size += 1
        else:
            root.left = insert(root.left, node)
            root.size += 1
    else:
        if root.right == None:
            root.right = node
            root.right.parent = root
            root.size += 1
        else:
            root.right = insert(root.right, node)
            root.size += 1
    if node.priority < root.priority:
        if node == root.left:
            root = right_rotate(root, root)
        elif node == root.right:
            root = left_rotate(root, root)
    return root        

def delete(root, val):
    pass

def inorder(root):
    l = []
    if root == None:
        return []
    else:
        l.extend(inorder(root.left))
        l.append((root.data, 'p:', root.priority, 's:', root.size))
        l.extend(inorder(root.right))
    return l

def get_size(node):
    if node == None:
        return 0
    else:
        return node.size
def find_node(root, val):
    if root == None:
        return root
    elif val < root.data:
        return find_node(root.left)
    elif val > root.data:
        return find_node(root.right)
    else:
        return root
        
def right_rotate(root, node):
    left_node = node.left # just deifne other node
    node.left = left_node.right # disconnecting node.left from other and connecting to left_node.right
    if left_node.right is not None: # if other.right is Not None then disconnect left_node.right.parent from other to node
        left_node.right.parent = node
    left_node.parent = node.parent # disconnecting other.parent from node to node.parent
    if node == root: # setting other as node.parent's child
        root = left_node
    elif node == node.parent.left:
        node.parent.left = left_node
    else:
        node.parent.right = left_node
    # now that we have exchanged the links and made 2 nodes independent we can rotate them 
    left_node.right = node
    node.parent = left_node
    node.size = 1 + get_size(node.left) + get_size(node.right)
    left_node.size = 1 + get_size(left_node.left) + get_size(left_node.right)
    return root
    
def left_rotate(root, node):
    right_node = node.right # define right node:
    node.right = right_node.left # disconnect node.right from right_node to right_node.left
    if right_node.left is not None: # if right node.left is not none then setting node as its parent
        right_node.left.parent = node
    right_node.parent = node.parent # setting right nodes parent as that of right node
    if node == root: # setting right_node as child of node.parent else as root
        root = right_node
    elif node == node.parent.right:
        node.parent.right = right_node
    else:
        node.parent.left = right_node
    # now we have disconnected all four links of parent and child, now we can rotate right node and node
    right_node.left = node
    node.parent = right_node
    node.size = 1 + get_size(node.left) + get_size(node.right)
    right_node.size = 1 + get_size(right_node.left) + get_size(right_node.right)
    return root
