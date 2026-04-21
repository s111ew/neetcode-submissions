# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast_ptr = dummy
        slow_ptr = dummy

        for _ in range(n):
            fast_ptr = fast_ptr.next

        while fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next
        
        slow_ptr.next = slow_ptr.next.next

        return dummy.next

        