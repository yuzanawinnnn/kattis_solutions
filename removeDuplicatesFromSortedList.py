class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode(float('-inf')) 
        while head:
            if cur.val != head.val:
                cur.next = head
                cur = cur.next
            head = head.next
        cur.next = None
            
        return dummy.next
        
