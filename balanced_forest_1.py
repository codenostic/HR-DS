# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 11:14:53 2017

@author: bhupeshgupta
"""

'''
Balanced forest
Input 
2 			-> Q i.e. 2 trees
5 			-> 5 node tree
1 2 2 1 1 		-> number of coins in each node
1 2 
1 3			-> connections 
3 5    		
1 4
3 			-> 3 node tree
1 3 5 			-> number of coins in each node
1 3			-> connections 
1 2

Output 
either Cw (if solution exists) else -1 

Description. 
Given a Tree of N nodes with each node having coins. 
Add another node with Cw coins.
Break tree into 3 Trees such that each tree has Equal Coins 

Solution
INPUT -             N, Nodes, Ci's - Coins, List_Node_Connections 
1) Possible_C3C2-   Input-Total Coins (CTotal). Output -(C3,C2) pairs, where 2*C2 + C3 = Ctotal and C3 < C2
2) Possible_C3s -   Input C3, OutPut - List possible combination of nodes with C3 coins = LIST_C3
3) Valid_C3s -      Input, LIST_C3 and List_Nodes_Connections, OUTPUT - List_Valid_C3
                    1) we have only one tree after Delete cominations of nodes in Step 2 -? 
                    2) Combination of nodes is a valid tree - ?
4) Possible_C2-     Input - C2, Output- Possible Combination of nodes = C2 Coins (= List_C2)
5) Valid_C2 -       Input - List_C2 and List_Node_Connections, Output - List_Valid_C2
6) Valid_C3C2-      Input - List_Valid_C2 & List_Valid_C3, Output - 2 C2s and 1 C3 with no node common in any

OUTPUT -           If Valid_C3C2 is success then Cw = C3-C2 else try next possible_C3C2, else -1

This solution itself cumbersome but needs considerable improvement when nodes 2000 and coins = 10**9
How -?
1) Use Clever Mathematics and deductions to Reduce possible  cases. Rather than brute force
2) Check which functions taking maximum time and optimize it. 

'''
import operator 
import itertools

def get_node_depth(node_links):
    '''
    Input 
    Node_links
    
    Output 
    Dictionary {depth: [nodes_list_atdepth]}
    '''
    stack = [(1,1)]
    result = {1:[1]}
    visited = set()
    while stack:
        node, depth = stack.pop()
        
        
    pass 

def get_depth_tree(node_links, node_depth):
    '''
    Input
    node_links - list of tuples
    node_depth - dictionary { depth:[nodes_list_atDepth]}
    
    Output 
    depth_tree -> {parentnode: list of childnodes in the tree at parent node}
    '''
    pass

def get_node_coins(node_links, coins_list, node_depth):
    '''
    Input
    node_links, coins_list, node_depth

    Output 
    Dictionary {node: coins under that node}
    
    '''
    pass

def C3C2(node_links, coin_list):
    '''
    this is main function which calls other fuunctions to finally give C3-C2 or -1 
    '''    
    node_depth = {}
    node_depth = get_node_depth(node_links)
    node_coins = {}
    node_coins = get_node_coins(node_links, coins_list, node_depth)
    sorted_coins = sorted(node_coins.items(), key=operator.itemgetter(1))
    group = itertools.groupby(sorted_coins, lambda x: x[1])
    coins_node_groups = []
    for key, nodes in group:
        coins_node_groups.append((key, [node[0] for node in nodes]))
    coin_node_dict = dict(coins_node_groups)
    CTotal = sum(coin_list)
    possible_C3C2 = []
    for C3 in coin_node_dict.keys():
        C2 = (CTotal - C3)//2
        if C2 not in coin_node_dict.keys():
            continue
        else:
            if len(coin_node_dict[C2]) >= 2:
                possible_C3C2.append({'C2':(C2, coin_node_dict[C2]), 'C3': (C3, coin_node_dict[C3])})
                
    return possible_C3C2

def balanced_forest(node_links, coin_list, depth_tree):
    '''
    Input
    node_links, coin_list

    Output 
    either C3-C2 if > 0 else -1        
    '''        
    possible_C3C2 = C3C2(node_links, coin_list)
    if len(possible_C3C2) == 0 :
        return -1
    valid_C3C2 = []
    while possible_C3C2:
        item = possible_C3C2.pop()
        C2_item, C3_item = item['C2'], item['C3']
        C2, C2_Nodes = C2_item
        C3, C3_Nodes = C3_item
        C2_trees_list = [lambda node: depth_tree[node] for node in C2_Nodes]
        C3_tree_list = [lambda node: depth_tree[node] for node in C3_Nodes]
        for tree in C3_tree_list:
            valid = sum([lambda item: 0 if len(set(item)-(set(item)-set(tree))) > 0 else 1 for item in C2_trees_list])
            if valid > 2:
                valid_C3C2.append(C2-C3)
            else:
                continue
        if valid_C3C2:            
            return min(valid_C3C2)
        else:
            -1
            
if __name__ == '__main__':
    Q = int(input()) #this gives number of tree < 5 but lets forget this for now 
    for _ in range(Q):
        
        N = int(input()) # number of nodes in tree 
        coins_list = [None] + [v for v in map(int, input().split())]
        node_links = []
        for _ in range(N-1):
            x, y = map(int, input().split())
            node_links.append((x,y))
        node_depth = get_node_depth(node_links)
        depth_tree = get_depth_tree(node_links, node_depth)
        print(balanced_forest(node_links, coins_list, depth_tree))
        













