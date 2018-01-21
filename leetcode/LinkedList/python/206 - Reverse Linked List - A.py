#https://leetcode.com/submissions/detail/101046109/

"""
Reverse Linked List
Difficulty: Easy

Reverse a singly linked list.

click to show more hints.

Hint:
A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """        
        """
        head      next
        [x: n] -> [y:n] -> [z: n] -> [w: n]
        
                  head      next
        [x: n] -> [y:n] -> [z: n] -> [w: n]
        
        ...
        
        new_head
        [w: n] -> [z: n] -> [y:n] -> [x: n]
        """ 
        new_head = None              
        while head: 
            curr = head           
            head = head.next
            curr.next = new_head
            new_head = curr
        return new_head