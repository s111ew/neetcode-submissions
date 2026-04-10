# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        head = list1
        main = list1
        to_merge = list2
        if list2.val < list1.val:
            head = list2
            main = list2
            to_merge = list1
        
        while main is not None and to_merge is not None:
            if main.next is None:
                main.next = to_merge
                return head
            if main.next.val < to_merge.val:
                main = main.next
            else:
                temp1 = main.next
                temp2 = to_merge.next
                main.next = to_merge
                to_merge.next = temp1
                to_merge = temp2
                main = main.next
        return head
        