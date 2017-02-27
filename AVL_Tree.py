# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 22:37:37 2017

@author: bhupeshgupta
"""

'''
AVL tree 
we will first implement AVL tree and then we will try to solve median. 
We will do this because AVL will help in lookup, add and delete in log N
also the balance factor is always -1,0,1
'''

# AVL Tree
# implement Insert, 
#Delete, Search a key, Traverse/print, rebalance, right rotation, left rotation, getbalance
# we are adding rank which is basically number of nodes in subtree rooted at NODE
# Also, Adding tree_median(root, size) which finds the median for tree
# to use AVL tree only remove MEDIAN, and RANK

class Node(object):
    def __init__(self, data, parent = None, left = None, right = None, height = 1, rank = 1):
        self.data = data 
        self.parent = parent 
        self.left = left
        self.right = right 
        self.height = height
        self.rank = rank

def insert(root, node):
    if root == None:
        root = node
    elif node.data < root.data:
        if root.left == None:
            root.left = node
            node.parent = root
            root.rank += 1
            if root.height == 1:            
                root.height += 1
        else:            
            root.left = insert(root.left, node)
            root.rank += 1
            if root.height == root.left.height:
                root.height += 1
    else:
        if root.right == None:
            root.right = node
            node.parent = root
            root.rank += 1 
            if root.height == 1:
                root.height += 1
        else:
            root.right = insert(root.right, node)
            root.rank += 1
            if root.height == root.right.height:
                root.height += 1       
    root = rebalance(root,node)
    return root

def rebalance(root, node):
    while node != root:
        node = node.parent
        BF_Node = get_balanceFact(node)
        if BF_Node > 1: # this means that it is right heavy
            # Case 1 - right child right heavy then left rotate node
            if get_balanceFact(node.right) > 0: 
                root = left_rotate(root, node)
            # Case 2 - right child left heavy, right rotate node.right and then left rotate node            
            elif get_balanceFact(node.right) < 0: 
                root =  right_rotate(root, node.right)
                root = left_rotate(root, node)
        elif BF_Node < -1: # this means tree is left heavy 
            # Case 3 - that left child is left heavy, then right rotate node
            if get_balanceFact(node.left) < 0: 
                root = right_rotate(root, node)
            # Case 4 -left child is right heavy, so left rotate node.left and right rotate node
            elif get_balanceFact(node.left) > 0: 
                root = left_rotate(root, node.left)
                root = right_rotate(root, node)
        else:
            continue
    return root
        
            

def get_node(root, data):
    if data == root.data:
        return root
    elif data < root.data:
        return get_node(root.left, data)
    else:
        return get_node(root.right, data)
        
def left_rotate(root, node):
    right_node = node.right
    node.right = right_node.left # copy right_node left subtree to node's right subtree 
    if right_node.left != None:
        right_node.left.parent = node    # also fixing right_node.left's parent as node
    right_node.parent = node.parent
    
    if node == root:
        root = right_node
    elif node == node.parent.left:
        node.parent.left = right_node
    else:
        node.parent.right = right_node
    right_node.left = node
    node.parent = right_node
    node.height = max(get_height(node.left), get_height(node.right)) +1
    node.rank = 1 + get_rank(node.left) + get_rank(node.right)
    right_node.height = max(get_height(right_node.left), get_height(right_node.right)) + 1         
    right_node.rank = 1 + get_rank(right_node.left) + get_rank(right_node.right)
    
    return root
    

def right_rotate(root, node):
    left_node = node.left
    node.left = left_node.right
    if left_node.right != None:
        left_node.right.parent = node
    left_node.parent = node.parent
    if node == root:
        root = left_node
    elif node == node.parent.left:
        node.parent.left = left_node
    else:
        node.parent.right = left_node
    left_node.right = node
    node.parent = left_node
    node.height = max(get_height(node.left), get_height(node.right)) + 1
    node.rank = 1 + get_rank(node.left) + get_rank(node.right)
    left_node.height = max(get_height(left_node.left), get_height(left_node.right)) + 1
    left_node.rank = 1 + get_rank(left_node.left) + get_rank(left_node.right)
    return root
    
def get_rank(node):
    if node == None:
        return 0
    else:
        return node.rank
        
def get_height(node):
    if node == None:
        return 0
    else:
        return node.height        

def tree_min(root):
    while root.left is not None:
        root = root.left
    return root

def tree_max(root):
    while root.right is not None:
        root = root.right
    return root

def delete(root, data):
    temp = None
    # root is None
    if root == None:
        node_del = False
        return root, node_del

    # cases 1 key < root.data 
    if data < root.data:
        if root.left != None:
            root.left = delete(root.left, data)
        else:
            node_del = False
    elif data > root.data:
        if root.right != None:
            root.right, node = delete(root.right, data)
        else:
            node_del = False
    else:
        if root.left == None and root.right == None:
            root = None
            node_del = True
        elif root.left == None:
            temp = root.right
            temp.parent = root.parent
            root = temp
            node_del = True
        elif root.right == None:
            temp = root.left
            temp.parent = root.parent
            root = temp
            node_del = True
        else:
            temp = tree_max(root.left)
            root.data = temp.data
            root.left = delete(root.left, temp.data)
            node_del = True

    if root == None and node_del == True:
        return root, node_del
    elif node_del == False:
        return root, node_del
    else:
        root.height = max(get_height(root.left), get_height(root.right)) + 1
        root.rank = 1 + get_rank(root.left) + get_rank(root.right)
        BF_root = get_balanceFact(root)
        if BF_root > 1: # this means that it is right heavy
            # Case 1 - right child right heavy then left rotate node
            if get_balanceFact(root.right) >= 0: 
                root = left_rotate(root, root)
            # Case 2 - right child left heavy, right rotate node.right and then left rotate node            
            elif get_balanceFact(root.right) < 0: 
                root =  right_rotate(root, root.right)
                root = left_rotate(root, root)
        elif BF_root < -1: # this means tree is left heavy 
            # Case 3 - that left child is left heavy, then right rotate node
            if get_balanceFact(root.left) <= 0: 
                root = right_rotate(root, root)
            # Case 4 -left child is right heavy, so left rotate node.left and right rotate node
            elif get_balanceFact(root.left) > 0: 
                root = left_rotate(root, root.left)
                root = right_rotate(root, root)
    
    return root, node_del

def node_successor(node):
    if node.right is not None:
        return tree_min(node.right)
    else:
        ancestor = node.parent
        while ancestor != None and node != ancestor.left:
            node = ancestor
            ancestor = ancestor.parent
        return ancestor

def node_pred(node):
    if node.left is not None:
        return tree_max(node.left)
    else:
        ancestor = node.parent
        while ancestor != None and node != ancestor.right:
            node = ancestor 
            ancestor = ancestor.parent
        return ancestor 
        
def get_balanceFact(node):
    if node.left == None and node.right == None:
        return 0
    elif node.left == None:
        return node.right.height
    elif node.right == None:
        return - node.left.height
    else:
        return node.right.height - node.left.height
        
def inorder(root):
    l = []
    if root == None:
        return []
    else:
        l += inorder(root.left)
        l.append((root.data, 'H:', root.height, 'R:', root.rank))
        l += inorder(root.right)
    return l 

def tree_median(root, size):
    if_odd = 1 if size%2 !=0 else 0
    rankdiff = get_rank(root.right) - get_rank(root.left)
    # if size is even or odd 
    if if_odd:
    # if size is odd get rankdiff 
    # if rankdiff = 0, root = root
        if rankdiff == 0:
            root = root
    # elif rankdiff > 0 =, for _ in range(0,rankdiff + 1, 2) root = node_successor(root)
        elif rankdiff > 0:
            for _ in range(0,rankdiff, 2):
                root = node_successor(root)
    # else for _ in range(0, abs(rankdiff) +1, 2), root = node_pred(root)
        else:
            for _ in range(0, abs(rankdiff), 2):
                root = node_pred(root)
#        return median = root.data
                
        return root.data
    # else:
    else:
    #   if rankdiff == 1, root = root, next_node = node_successor(root)
        if rankdiff == 1:
            root = root
            next_node = node_successor(root)
    #   elif rankdiff == -1 root = root,next_node = node_pred(root)
        elif rankdiff == -1:
            root = root
            next_node = node_pred(root)
    #   elif rankdiff > 1 for _ in range(0, rankdiff, 2): root = node_successor(root), next_node = node_succes(root)
        elif rankdiff > 1:
            for _ in range(0,rankdiff -2, 2):
                root = node_successor(root)
                next_node = node_successor(root)
    # elif rankdiff < -1 for _in range(0,abs(rankdiff), 2): root = node_pred, next_node = node_pred
        elif rankdiff < -1:
            for _ in range(0,abs(rankdiff) -2, 2):
                root = node_pred(root)
                next_node = node_pred(root)
    # median = (root.data + next_node.data)/2
        return (root.data + next_node.data)/2
    
def rTree_median(root, leftRank, rightRank):
    rank_diff = rightRank - leftRank
    if rank_diff == 0:
        mid_node = root
        median = mid_node.data
    elif rank_diff == 1:
        mid_node = root
        next_node = tree_min(root.right)
        median = (mid_node.data + next_node.data)/2
    elif rank_diff == -1:
        mid_node = root
        next_node = tree_max(root.left)
        median = (mid_node.data + next_node.data)/2
    elif rank_diff > 1:
        next_root = root.right 
        next_node_leftRank = get_rank(next_root.left) 
        newLeftRank = leftRank + 1 + next_node_leftRank
        newRightRank = rightRank - 1 - next_node_leftRank
        median = rTree_median(next_root, newLeftRank, newRightRank)
    else:
        next_root = root.left 
        next_node_rightRank = get_rank(next_root.right) 
        newRightRank = rightRank + 1 + next_node_rightRank
        newLeftRank = leftRank - 1 - next_node_rightRank
        median = rTree_median(next_root, newLeftRank, newRightRank)
    return median 
        
        
    pass