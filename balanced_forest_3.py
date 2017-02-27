# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 17:46:22 2017

@author: bhupeshgupta
"""

'''
using undirected graphs 
Making list in list 

'''
import collections
import operator
import itertools

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


def get_depth_tree_atNode(nodes_atDepth,node_tree,N):
    depth_tree_dict = {}
    node_tree = [None if X == [] else X for X in node_tree]
    for nodes_atD in nodes_atDepth[::-1]:
        for node_atD in nodes_atD:
            if node_tree[node_atD] is None:
                depth_tree_dict[node_atD] = [node_atD]
            else:
                connected_nodes = node_tree[node_atD]
                list_trees_connectedNodes = []
                for connecting_node in connected_nodes:
                    list_trees_connectingNode = []
                    for X in depth_tree_dict[connecting_node]:
                        list_trees_connectingNode.append(([node_atD] + X) if isinstance(X,list) else ([node_atD]+[X]))
                    list_trees_connectedNodes.extend(list_trees_connectingNode)
                depth_tree_dict[node_atD] = list_trees_connectedNodes[:]
    return depth_tree_dict

def get_depth_coins(depth_tree,coins_list):
    coins_dict = {}
    trees_list = []
    for key in depth_tree.keys():
        trees_list += [X if isinstance(X, list) else [X] for X in depth_tree[key]]
    for item in trees_list:
        coins_dict[tuple(item)] = sum([coins_list[X] for X in item])
    return coins_dict


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
    C2 = CTotal//2 
    if C2 in coin_node_dict.keys() and len(coin_node_dict[C2]) == 2:
        possible_C3C2.append({'C2':(C2, coin_node_dict[C2]), 'C3': (0, [()])})
    for C3 in coin_node_dict.keys():
        C2 = (CTotal - C3)//2
        if C2 not in coin_node_dict.keys():
            continue
        elif C3 >= C2:
            continue
        else:
            if len(coin_node_dict[C2]) >= 2:
                possible_C3C2.append({'C2':(C2, coin_node_dict[C2]), 'C3': (C3, coin_node_dict[C3])})

    return possible_C3C2 

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
        print(C2_trees_list, 'C2_trees', C3_trees_list, 'C3_trees')
        for tree in C3_trees_list:
            valid = [ 0 if len(set(item)-(set(item)-set(tree))) > 0 else 1 for item in C2_trees_list]
            if sum(valid) >= 2:
                valid_C3.append(((C2-C3),C2_trees_list))
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
        print(valid_C3C2, 'Valid_C3C2')
    if len(valid_C3C2) > 0:            
        return min(valid_C3C2)[0]
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
    print(node_tree, 'Node_tree')
    nodes_atDepth = get_node_depth(node_tree, N)
    print(nodes_atDepth, 'Nodes_atDepth')
    depth_tree = get_depth_tree_atNode(nodes_atDepth,node_tree, N)
    print(depth_tree, 'depth_trees')
    coins_dict = get_depth_coins(depth_tree, coins_list)
    print(coins_dict, 'coins_dict')
    possible_C3C2 = get_possible_C3C2(coins_dict)
    print(possible_C3C2, 'possible_C3C2')
    print(valid_Cw_list(possible_C3C2))
#node_tree = [None, [2, 4], [3], [], [5], [6, 7], [], [8], []]
#nodes_atDepth =  [None, [1], [2, 4], [3, 5], [6, 7], [8], None, None, None]
#print(get_depth_tree_atNode(nodes_atDepth, node_tree, 8))