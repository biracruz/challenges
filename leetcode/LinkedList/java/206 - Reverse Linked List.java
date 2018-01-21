//https://leetcode.com/submissions/detail/115862506/

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode newHead =  null;
        while (head != null){
            ListNode tmp = head;
            head = head.next;
            tmp.next = newHead;
            newHead = tmp;
            
        }
        return newHead;
    }
}