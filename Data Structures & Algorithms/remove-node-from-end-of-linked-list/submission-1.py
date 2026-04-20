# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Naive solution O(n) Space
        nodes = []
        curr = head
        while curr is not None:
            nodes.append(curr)
            curr = curr.next
        if len(nodes) == 1:
            return None

        to_remove = nodes[len(nodes) - n]
        if len(nodes) - n == 0:
            head = to_remove.next
        else:
            prev = nodes[len(nodes) - n - 1]
            prev.next = to_remove.next
        return head