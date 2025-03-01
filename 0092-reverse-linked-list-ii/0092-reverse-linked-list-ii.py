# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode()
        dummy.next = head
        prev = dummy 
        for _ in range(left - 1):
            prev = prev.next
        
        curr = prev.next
        for _ in range(right - left):
            new_node = curr.next
            curr.next, prev.next, new_node.next = new_node.next, new_node, prev.next

        return dummy.next