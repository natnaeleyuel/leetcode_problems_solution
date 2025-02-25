# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        c = 0
        curr = dummy
      
        while l1 or l2 or c:
            sum_ = (l1.val if l1 else 0) + (l2.val if l2 else 0) + c
            c, val = divmod(sum_, 10)
            curr.next = ListNode(val)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
      
        return dummy.next 