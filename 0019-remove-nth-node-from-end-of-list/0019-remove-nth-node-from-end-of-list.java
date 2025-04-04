

class Solution 
{
    public ListNode removeNthFromEnd(ListNode head, int n) 
    {
        if(head.next==null)
            return null;
        ListNode dummy=new ListNode();
        dummy.next=head;
        ListNode slow=dummy;
        ListNode fast=dummy;
        
        for(int i=1;i<=n;i++)
            fast=fast.next;
        
        while(fast.next!=null)
        {
            fast=fast.next;
            slow=slow.next;
        }
        
        slow.next=slow.next.next;
        return dummy.next;
    }
}