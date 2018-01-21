"""
Reverse Linked List
Difficulty: Easy

Reverse a singly linked list.

click to show more hints.

Hint:
A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

class Solution:
# @param {ListNode} head
# @return {ListNode}
def reverseList(self, head):
    return self._reverse(head)

def _reverse(self, node, prev=None):
    if not node:
        return prev
    n = node.next
    node.next = prev
    return self._reverse(n, node)