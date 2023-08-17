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
    ListNode reverse(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }

        ListNode newNode = reverse(head.next);
        head.next.next = head;
        head.next = null;
        return newNode;
    }

    public ListNode reverseBetween(ListNode head, int left, int right) {
        if (head == null || head.next == null) {
            return head;
        }
        ListNode dummy = new ListNode(1);
        dummy.next = head;
        ListNode temp = dummy;
        ListNode node = head;
        int count = 1;
        while (count < left) {
            temp = node;
            node = node.next;
            count++;
        }
        ListNode temp2 = node;
        while (count < right) {
            temp2 = temp2.next;
            count++;
        }
        ListNode last = temp2.next;
        temp2.next = null;
        temp.next = reverse(node);
        node.next = last;
        return dummy.next;
    }
}
