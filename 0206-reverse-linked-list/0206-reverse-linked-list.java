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
    public ListNode reverseList(ListNode head) {
        ListNode pr,cur,nex;
        if (head==null || head.next==null){
            return head;
        }
        pr=null;
        cur=head;
        nex=cur.next;
        while(cur.next!=null){
            cur.next=pr;
            pr=cur;
            cur=nex;
            nex=cur.next;
        }
        cur.next=pr;
        return cur;
    }
}