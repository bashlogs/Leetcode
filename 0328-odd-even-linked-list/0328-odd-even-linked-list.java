
class Solution {
    public ListNode oddEvenList(ListNode head) {
        if(head == null || head.next == null){
            return head;
        }
        ListNode temp = head;
        ListNode end = head;
        int count = 0;
        while(end.next != null){
            count++;
            end = end.next;
        }
       
        count = (count%2 == 0) ? count/2 : count/2+1;

        while(count-- > 0){
            end.next = temp.next;
            temp.next = temp.next.next;
            end.next.next = null;
            temp = temp.next;
            end = end.next;
        }
        return head;
    }
}