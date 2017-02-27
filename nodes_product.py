# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 10:55:58 2017

@author: bhupeshgupta
"""

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
        print(tree_list1, tree_list2)
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
            print(tree_list1, tree_list2)
            for item_tree1 in tree_list1:
                for item_tree2 in tree_list2:
                    combined_item = item_tree1 + item_tree2
                    product_list.append(combined_item)
            if len(node_list) == 0:
                product_list = [item + [node] for item in product_list]
                return product_list
            else:
                node_list.append(product_list)
            
#Inputs 
node1 = 7
node1_combo1 = [[[6]]]
node1_combo2 = [[[5]]]
node1_combo3 = [[[5]],[[6]]]

node2 = 2
node2_combo1 = [[[3]]]

node3 = 8
node3_combo1 = [[[6,7], [5,7], [5,6,7]]]

node4 = 1
node4_combo1 = [[[2,3], [2]]]
node4_combo2 = [[[4]]]
node4_combo3 = [[[6,7,8], [5,7,8], [5,6,7,8], [8]]]
node4_combo4 = [[[2,3],[2]], [[4]]]
node4_combo5 = [[[2,3], [2]], [[5,7,8], [6,7,8], [5,6,7,8], [8]]]
node4_combo6 = [[[4]],[[5,7,8],[6,7,8],[5,6,7,8], [8]]]
node4_combo7 = [[[2,3], [2]], [[4]], [[5,7,8],[7,6,8], [5,6,7,8], [8]]]

#outputs
#print('input', (node1, node1_combo1), 'output', nodes_product(node1, node1_combo1))
#print('input', (node1, node1_combo2), 'output', nodes_product(node1, node1_combo2))
#print('input', (node1, node1_combo3), 'output', nodes_product(node1, node1_combo3))
#print('input', (node2, node2_combo1), 'output', nodes_product(node2, node2_combo1))
#print('input', (node3, node3_combo1), 'output', nodes_product(node3, node3_combo1))
#print('input', (node4, node4_combo1), 'output', nodes_product(node4, node4_combo1))
#print('input', (node4, node4_combo2), 'output', nodes_product(node4, node4_combo2))
#print('Input', (node4, node4_combo3), 'output', nodes_product(node4, node4_combo3))
#print('Input', (node4, node4_combo4), 'output', nodes_product(node4, node4_combo4))
#print('input', (node4, node4_combo5), 'output', nodes_product(node4, node4_combo5))
#print('Input', (node4, node4_combo6), 'output', nodes_product(node4, node4_combo6))
print('input', (node4, node4_combo7), 'output', nodes_product(node4, node4_combo7))
