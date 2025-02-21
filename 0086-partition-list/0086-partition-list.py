class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_node_head = ListNode()
        large_node_head = ListNode()

        less_node_tail = less_node_head
        large_node_tail = large_node_head

        current = head
        while current:
            if current.val < x:
                less_node_tail.next = current
                less_node_tail = less_node_tail.next
            else:
                large_node_tail.next = current
                large_node_tail = large_node_tail.next
            current = current.next
        less_node_tail.next = large_node_head.next
        large_node_tail.next = None

        return less_node_head.next


        
