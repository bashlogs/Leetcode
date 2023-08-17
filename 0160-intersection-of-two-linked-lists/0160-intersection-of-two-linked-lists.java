/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        int count = 0;
        ListNode tempA = headA;
        ListNode tempB = headB;

        while(tempB != null){
            if(tempA == null){
                tempB = tempB.next;
                tempA = headA;
            }
            if(tempA == tempB){
                return tempA;
            }
            tempA = tempA.next;
        }

        return tempB;
    }
}