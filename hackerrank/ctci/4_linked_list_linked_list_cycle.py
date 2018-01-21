#https://www.hackerrank.com/challenges/ctci-linked-list-cycle/problem
"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

def has_cycle(head):
    visited = {}
    node = head.next
    while node:
        if visited.get(node.data):
            #already visited
            return True
        else:
            visited[node.data] = True
            node = node.next
    return False