//https://leetcode.com/submissions/detail/115713169/

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */


class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode a = l1;
        ListNode b = l2;
        ListNode head = new ListNode(-1);
        ListNode curr = head;
        while (a != null && b != null){
            if (a.val > b.val){
                ListNode tmp = a;
                a = b;
                b = tmp;
            }
            curr.next = a;
            a = a.next;
            curr = curr.next;            
        }
        
        if (a != null){
            curr.next = a;
        }
        
        if (b != null){
            curr.next = b;
        }
        return head.next;
    }
}