# https://leetcode.com/submissions/detail/115678607/

'''
Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.
'''




# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a, b = l1, l2
        head = ListNode(-1)
        curr = head
        while a and b:
            #put the bigger on 'a'
            if a.val > b.val:
                a, b = b, a            
            #just travel or point to the bigger
            curr.next = a 
            a = a.next            
            curr = curr.next
        curr.next = a or b
        
        return head.next