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
    public int print(ListNode head){
        int cal = 0;
        while(head != null){
            System.out.println(head.val);
            head = head.next;
            cal += 1;
        }
        return cal;
    }

    public int count(ListNode head){
        int cal = 0;
        while(head != null){
            head = head.next;
            cal += 1;
        }
        return cal;
    }

    ListNode r2 = null;
    public int check(ListNode l1, ListNode r1){
        int ans = 0;
        int ans1 = 0;
        if(l1.next == null){
            return l1.val + r1.val;
        }
        else{
            ans = check(l1.next, r2);
            r2 = r2.next;
            ans1 = l1.val + r2.val;
            System.out.println(ans+" "+ans1);
            return Math.max(ans,ans1);
        }
    }

    public int pairSum(ListNode head) {
        ListNode temp = head;
        ListNode l1 = temp;
        ListNode r1 = null;
        int ans = 0;
        int cal = count(l1);
        int count = 0;
        while(count < cal/2-1){
            l1 = l1.next;
            count++;
        }
        r1 = l1.next;
        l1.next = null;
        // System.out.println(cal);

        // print(r1);
        r2 = r1;
        ans = check(temp,r1);
        return ans;
    }
}