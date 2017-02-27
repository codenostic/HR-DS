# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 17:05:44 2017

@author: bhupeshgupta
"""
import itertools

def get_node_combinations(node_list):
    node_combos = []
    list_n = []
    for n in range(1, len(node_list)+1):
        list_n = list(itertools.combinations(node_list, n))
        node_combos.extend(list_n)
    return node_combos

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

nodes_atDepth = [[1], [2, 4, 8], [3, 7], [6, 5]]
node_tree = [None, [2, 4, 8], [3], [], [], [], [], [6, 5], [7]]
print(depth_tree_atNode(nodes_atDepth, node_tree, 8))