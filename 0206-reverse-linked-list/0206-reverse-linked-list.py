class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode()
        current_node = head
        while current_node:
            next_node = current_node.next
            current_node.next = dummy_node.next
            dummy_node.next = current_node
            current_node = next_node
        return dummy_node.next