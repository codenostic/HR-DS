# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 16:41:57 2017

@author: bhupeshgupta
"""

class Node(object):
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node
    
    def Insert(self, data):
        new_node = Node(data)
        if self is None:
            self = new_node
        else:
            node = self
            while node.next is not None:
                node = node.next
            node.next = new_node
        return self
    
    def print_list(self):
        while self is not None:
            print(self.data)
            self = self.next
    
    def Delete(self, position):
        if position == 0:
            self = self.next
        elif position == 1:
            self.next = self.next.next
        else:
            node = self
            for _ in range(position):
                prev_node = node
                node = node.next
            prev_node.next = node.next
        return self
          
    def Reverse(self):
        if self is None:
            return self
        elif self.next is None:
            return self
        else:
            self = self.next.Reverse().Insert(self.data)
        return self
  
    def Revese2(self):
        prev_node = None
        cur_node = self
        next_node = self.next 
        
        pass
    
    def CompareLists(self, other):
        if self is None and other is None:
            return 1
        elif self is None and other is not None:
            return 0
        elif self is not None and other is None:
            return 0 
        elif self.data != other.data:
            return 0 
        else:
            return self.next.CompareLists(other.next)
            
    def MergeLists(self, other):
        if self is None and other is None:
            return None
        elif self.next is None:
            return self
        elif other.next is None:
            return other

        new_head = Node
        if self.data < other.data:
            new_head = self
            new_head.next = self.next.MergeLists(other)
        else:
            new_head = other 
            new_head.next = other.next.MergeLists(self)
        return new_head
    
    def RemoveDuplicates(self):
    
        if self is None or self.next is None:
            return self
        elif self.data == self.next.data:
            self.Delete(1)
            self = self.RemoveDuplicates()
        else:
            self.next = self.next.RemoveDuplicates()
        return self

    def has_cycle(self):
        pass
    
    def FindMergeNode(self, other):
        pass