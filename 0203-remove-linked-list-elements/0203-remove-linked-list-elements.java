/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeElements(ListNode head, int val) {
        ListNode dummy = new ListNode(1);
        dummy.next = head;
        ListNode temp = dummy;
        ListNode n1 = temp.next;

        while(n1 != null){
            if(n1.val == val){
                temp.next = n1.next;
            }
            else{
                temp = temp.next;
            }
            n1 = n1.next;
        }
        return dummy.next;
    }
}