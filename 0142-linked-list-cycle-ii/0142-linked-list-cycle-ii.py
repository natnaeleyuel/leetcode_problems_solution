# class ListNode:
#     def __init__(self, x=0):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        iscycle = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                iscycle = True
                break

        slow = head
        while iscycle:
            if slow == fast:
                return fast
            slow = slow.next
            fast = fast.next
        return None
            