# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):        
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head:        
            #{label: Node }
            copy = {}
            curr = head
            while curr:
                copy[curr.label] = RandomListNode(curr.label)
                curr = curr.next            
            
            curr = head
            while curr:
                if curr.next:
                    copy[curr.label].next = copy[curr.next.label]
                if curr.random:
                    copy[curr.label].random = copy[curr.random.label]
                curr = curr.next
            
            ref = copy[head.label]
            return ref                                                
        else:
            return head