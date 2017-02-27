# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 19:13:27 2017

@author: bhupeshgupta
"""

def get_nodes_atDepth(node_links, N):
    nodes_atDepth = [None, [1]] + [None]*(N-1)
    for depth in range(1, N):
        nodedepth_list = nodes_atDepth[depth]
        if len(nodedepth_list) == 0:
            break
        if nodes_atDepth[depth+1] is None:
            nodes_atDepth[depth+1] = []
        for node_atdepth in nodedepth_list:
             node_d1 = node_links[node_atdepth]
             if node_d1 is None:
                 continue
             for node in node_d1:
                 nodes_atDepth[depth+1].append(node)
        
    nodes_atDepth[depth] = None
#    print(nodes_atDepth)
    return nodes_atDepth    

def get_depth_tree(node_links, coins_list, N):
    nodes_atDepth = get_nodes_atDepth(node_links, 5)
    depth_tree = [None]*(N+1)
    for nodes_listatD in nodes_atDepth[::-1]:
        if nodes_listatD is None:
            continue
        else:
            for node_atD in nodes_listatD:
                connected_nodes_list = node_links[node_atD]
                if connected_nodes_list is None:
                    item = {}
                    item[str(node_atD)] = coins_list[node_atD]
                    depth_tree[node_atD] = item
                else:
                    for node in connected_nodes_list:
                        node_dict = depth_tree[node]
                        if node_dict is None:
                            node_dict = {}
                            node_dict[str(node_atD) + str(node)] = depth_tree[node] + coins_list[node_atD]
                        else:
                            temp = {}
                            for key in node_dict.keys():
                            
                                temp[str(node_atD)+key] = (node_dict[key]+coins_list[node_atD])
                            if depth_tree[node_atD] is None:
                                depth_tree[node_atD] = {}
                                depth_tree[node_atD].update(temp)
                            else:
                                depth_tree[node_atD].update(temp)
                        
    print(depth_tree)
    return depth_tree

def get_tree_coins(depth_tree):
    node_tree_coins = {}
    for dict_item in depth_tree:
        if dict_item is None: 
            continue
        else:
            node_tree_coins.update(dict_item)
            
#    print(node_tree_coins)
    return node_tree_coins
import operator
import itertools

def get_possible_C3C2(node_links, coins_list, N):
    depth_tree = get_depth_tree(node_links, coins_list, N)
    node_tree_coins = get_tree_coins(depth_tree)  
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
    for C3 in coin_node_dict.keys():
        C2 = (CTotal - C3)//2
        if C2 not in coin_node_dict.keys():
            continue
        elif C3 >= C2:
            continue
        else:
            if len(coin_node_dict[C2]) >= 2:
                possible_C3C2.append({'C2':(C2, coin_node_dict[C2]), 'C3': (C3, coin_node_dict[C3])})

    print(possible_C3C2)
    return possible_C3C2




node_links = [None, [2, 3, 4], None, [5], None, None]
coins_list = [None, 1, 2, 2, 1, 1]
node_depth = get_nodes_atDepth(node_links, 5)
depth_tree = get_depth_tree(node_links, coins_list, 5)
node_tree_coins = get_tree_coins(depth_tree)
possible = get_possible_C3C2(node_links, coins_list, 5)
#node_depth1 = get_node_depth(node_links1)