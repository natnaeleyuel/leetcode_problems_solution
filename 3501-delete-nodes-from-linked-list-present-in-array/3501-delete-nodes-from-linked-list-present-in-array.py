# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        start = None
        num_set = set(nums)
        while curr != None:
            if curr.val in num_set:
                if prev:
                    prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
            if not start and prev:
                start = prev
        return start
