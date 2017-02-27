# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 12:20:41 2017

@author: bhupeshgupta
"""
import itertools

#def get_depth_tree_atNode(nodes_atDepth,node_tree,N):
#    depth_tree_dict = {}
#    node_tree = [None if X == [] else X for X in node_tree]
#    for nodes_atD in nodes_atDepth[::-1]:
#        for node_atD in nodes_atD:
#            if node_tree[node_atD] is None:
#                depth_tree_dict[node_atD] = [node_atD]
#            else:
#                connected_nodes = node_tree[node_atD]
#                list_trees_connectedNodes = []
#                for connecting_node in connected_nodes:
#                    list_trees_connectingNode = []
#                    for X in depth_tree_dict[connecting_node]:
#                        list_trees_connectingNode.append(([node_atD] + X) if isinstance(X,list) else ([node_atD]+[X]))
#                    list_trees_connectedNodes.extend(list_trees_connectingNode)
#                depth_tree_dict[node_atD] = list_trees_connectedNodes[:]
#    return depth_tree_dict

def get_node_combinations(node_list):
    node_combos = []
    list_n = []
    for n in range(1, len(node_list)+1):
        list_n = list(itertools.combinations(node_list, n))
        node_combos.extend(list_n)
    return node_combos

node_list = [2, 4, 8]
#print(get_node_combinations(node_list))

def nodes_product(node, *args):
    list_c = list(itertools.product(args))
#    print(list_c)
    for i in range(len(list_c)):
        item_list_i = []
        temp_items = list_c[i]
        for item in temp_items:
            if isinstance(item, list):
                item_list_i.extend(item)
            else:
                
                item_list_i.append(item)
        item_list_i.append(node)
        list_c[i] = item_list_i[:]
    return list_c

a = [[2,3]]
b = [[8,7,6], [8,7,5], [8,7,5,6]]
c = [4]
args = [a,b,c]

#args = [6,5]
#print(nodes_product(1, *args))  

def get_depth_tree_atNode(nodes_atDepth, node_tree, N):
    depth_tree_dict = {}
    node_tree = [None if X == [] else X for X in node_tree]
    for nodes_list_atD in nodes_atDepth[::-1]:
        for node_atD in nodes_list_atD:
            if node_tree[node_atD] is None:
                depth_tree_dict[node_atD] = [node_atD]
            else:
                connected_nodes_list = node_tree[node_atD]
#                print(node_atD, connected_nodes_list)
                node_combos = get_node_combinations(connected_nodes_list)
#                print(node_atD, node_combos)
                for combo_n in range(len(node_combos)):
                    combo_node_list = node_combos[combo_n]
#                    tree_list_combo = [depth_tree_dict[node] for node in combo_node_list]
                    tree_list_combo = []                    
                    for node in combo_node_list:
                        tree_list_combo.extend(depth_tree_dict[node])
                    print(node_atD, tree_list_combo)
                    product_list_combo = []
                    for item in nodes_product(node_atD, tree_list_combo ):
                        product_list_combo.append(item)
#                    print(combo_node_list, product_list_combo)
                    node_combos[combo_n] = product_list_combo[:]
                connect_nodes_extend = []
                for item in node_combos:
                    connect_nodes_extend.extend(item)
                depth_tree_dict[node_atD] = connect_nodes_extend
    return depth_tree_dict
    
nodes_atDepth = [[1], [2, 4, 8], [3, 7], [6, 5]]
node_tree = [None, [2, 4, 8], [3], [], [], [], [], [6, 5], [7]]
print(get_depth_tree_atNode(nodes_atDepth, node_tree, 8))


