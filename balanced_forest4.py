# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 19:21:34 2017

@author: bhupeshgupta
"""

import collections
import operator
import itertools
import time

def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print ('%s function took %0.3f ms' % (f.__name__ , (time2-time1)*1000.0))
        return ret
    return wrap

def make_tree(node_links, N):
    tree = [None]+ [[] for n in range(N)]
    inserted = set([1])
    node_links = collections.deque(node_links)
    while node_links:
        x,y = node_links.popleft()
        if x in inserted:
            tree[x].append(y)
            inserted.add(y)
        elif y in inserted:
            tree[y].append(x)
            inserted.add(x)
        else: 
            node_links.append((x,y))
    return tree

def get_node_depth(nodes_tree, N):
    nodes_atDepth = [None]*(N+1)
    stack = collections.deque([(1,1)])
    while stack:
        node, depth = stack.pop()
        if nodes_atDepth[depth] is None:
            nodes_atDepth[depth] = [node]
        else: 
            nodes_atDepth[depth] += [node]
        for node in nodes_tree[node]:
            if node == []:
                continue
            else:
                stack.appendleft((node,depth+1))
    return list(filter((None).__ne__, nodes_atDepth))

def get_node_combinations(node_list):
    node_combos = []
    list_n = []
    for n in range(1, len(node_list)+1):
        list_n = list(itertools.combinations(node_list, n))
        node_combos.extend(list_n)
    return node_combos
#@timing
def nodes_product(node, *args):
    node_list = list(*args)
#    print(node_list)
    
    if len(node_list) == 1:
        product_list = []
        tree_list = node_list.pop()
        for tree in tree_list:
            node_tree = tree + [node]
            product_list.append(node_tree)
        return product_list
    elif len(node_list) == 2:
        product_list = []
        tree_list1 = node_list.pop()
        tree_list2 = node_list.pop()
        for item_tree1 in tree_list1:
            for item_tree2 in tree_list2:
                combined_item = item_tree1 + item_tree2 + [node]
                product_list.append(combined_item)
        return product_list
    else:
        while node_list:
            product_list = []
            tree_list1 = node_list.pop()
            tree_list2 = node_list.pop()
            for item_tree1 in tree_list1:
                for item_tree2 in tree_list2:
                    combined_item = item_tree1 + item_tree2
                    product_list.append(combined_item)
            if len(node_list) == 0:
                product_list = [item + [node] for item in product_list]
                return product_list
            else:
                node_list.append(product_list)
 
#@timing
def depth_tree_atNode(nodes_atDepth, node_tree, N):
    # initialize a dict 
    depth_tree_dict = {}
    # for all nodes at Depth D pick a node at D
    node_tree = [None if X == [] else X for X in node_tree]
    while nodes_atDepth:
        nodesList_atD = nodes_atDepth.pop()
    # for this Node at depth D check nodes connected to it
        for aNode_atD in nodesList_atD:
            tree_list = []            
            connected_nodes_list = node_tree[aNode_atD]
            
    # if No nodes are connected then node is a leaf -> hence just add this to dictionary
            if connected_nodes_list == None:
                tree = [aNode_atD]
                tree_list = tree_list + [tree]
                depth_tree_dict[aNode_atD] = tree_list
    # else make a list of connected_nodes 
    # if only one connected node then find the tree list for this connected node 
            elif len(connected_nodes_list) == 1:
                connected_node = connected_nodes_list.pop()
                node_tree_list = depth_tree_dict[connected_node]
                # add Node at depth D to each tree in this tree_list
                tree_list = [tree + [aNode_atD] for tree in node_tree_list]
                tree_list += [[aNode_atD]]
                depth_tree_dict[aNode_atD] = tree_list
                
    # if connected nodes more than 1 then make combinations of connected nodes
            else:
#                print(connected_nodes_list)
                connected_nodes_combos = get_node_combinations(connected_nodes_list)
    # as each combination is a valid tree. Store this combinations in nodes_combo_lists
                possible_combinations = []            
                for aCombo in connected_nodes_combos:                
    # for each valid combination select a nodes_list
    # for this particular nodes_list populate the node_tree_list of each node from dict
                    node_tree_list = [depth_tree_dict[node] for node in aCombo]

    # combine a nodes in a tree from particular tree_list with all other trees in other node_tree_lists
                    tree_list_aCombo = nodes_product(aNode_atD, node_tree_list)
    # once combined_tree_list is for a particular combination,
                    possible_combinations += tree_list_aCombo 
    # do this for each combination and then we get all possible_combinations for connected nodes
    # save this list of possible_combinations to the dictiionary for node_atD
                possible_combinations += [[aNode_atD]]
                depth_tree_dict[aNode_atD] = possible_combinations
    # like this keep doing for all nodes_atDepth D, D-1, D-2 so on........ 
    # return dict 
    return depth_tree_dict
    
def get_depth_coins(depth_tree,coins_list):
    coins_dict = {}
    trees_list = []
    for key in depth_tree.keys():
        trees_list += [X if isinstance(X, list) else [X] for X in depth_tree[key]]
    for item in trees_list:
        coins_dict[tuple(item)] = sum([coins_list[X] for X in item])
    return coins_dict

#@timing
def get_possible_C3C2(coins_dict):
    node_tree_coins = coins_dict
    sorted_coins = sorted(node_tree_coins.items(), key=operator.itemgetter(1))
    group = itertools.groupby(sorted_coins, lambda x: x[1])
    coins_node_groups = []
    for key, nodes in group:
        coins_node_groups.append((key, [node[0] for node in nodes]))
    coin_node_dict = dict(coins_node_groups)
    CTotal = 0    
    for X in coins_list:
        if X is not None:
            CTotal += X
    possible_C3C2 = []
    if (CTotal%2 == 0) and  ((CTotal//2) in coin_node_dict.keys()) and len(coin_node_dict[CTotal//2]) == 2:
        C2 = CTotal//2 
        possible_C3C2.append({'C2':(C2, coin_node_dict[C2]), 'C3': (0, [()])})
    for C3 in coin_node_dict.keys():
        C2 = (CTotal - C3)//2
        if C2 not in coin_node_dict.keys():
            continue
        elif C3 >= C2:
            continue
        else:
            if len(coin_node_dict[C2]) >= 2 and ((2*C2 + C3) == CTotal):
                possible_C3C2.append({'C2':(C2, coin_node_dict[C2]), 'C3': (C3, coin_node_dict[C3])})

    return possible_C3C2 
#@timing
def valid_Cw_list(possible_C3C2):

    if len(possible_C3C2) == 0 :
        return -1
    valid_C3 = []
    valid_C3C2 = []
    while possible_C3C2:
        item = possible_C3C2.pop()
        C2_item, C3_item = item['C2'], item['C3']
        C2, C2_trees_list = C2_item
        C3, C3_trees_list = C3_item
#        print(C2_trees_list, 'C2_trees', C3_trees_list, 'C3_trees')
        for tree in C3_trees_list:
            valid = [ 0 if len(set(item)-(set(item)-set(tree))) > 0 else 1 for item in C2_trees_list]
            if sum(valid) >= 2:
                valid_C3.append(((C2-C3),C2_trees_list))
                break
            else:
                continue
#        print(valid_C3, 'Valid_C3')
        
        for Cw, C2_trees_list in valid_C3:

            temp_C2_trees = C2_trees_list[:]
#            print(C2_trees_list, 'again print C2_trees', temp_C2_trees, 'temp_c2')
            for tree in C2_trees_list:
                valid = [ 0 if len(set(item)-(set(item)-set(tree))) > 0 else 1 for item in temp_C2_trees]
#                print(valid, 'valid_c3c2')
                if sum(valid) >= 1:
                    valid_C3C2.append((Cw, [item, tree]))
                    break
#    print(valid_C3C2, 'Valid_C3C2')
    if len(valid_C3C2) > 0:            
        return min(valid_C3C2, key = operator.itemgetter(0))[0]
    else:
        return -1

#input and main function 
Q = int(input()) # number of trees 
for _ in range(Q):
    N = int(input()) # number of nodes 
    node_links = []
    coins_list = [None] + [coins for coins in map(int, input().split())]
    for i in range(N - 1):                
        node_links.append(tuple(map(int, input().split())))
    

    node_tree = make_tree(node_links, N)
#    print(node_tree, 'Node_tree')
    nodes_atDepth = get_node_depth(node_tree, N)
#    print(nodes_atDepth, 'Nodes_atDepth')
    depth_tree = depth_tree_atNode(nodes_atDepth,node_tree, N)
#    print(depth_tree, 'depth_trees')
    coins_dict = get_depth_coins(depth_tree, coins_list)
    print(sorted(coins_dict.items(), key = operator.itemgetter(1)), 'coins_dict')
    possible_C3C2 = get_possible_C3C2(coins_dict)
#    print(possible_C3C2, 'possible_C3C2')
#    print(valid_Cw_list(possible_C3C2))