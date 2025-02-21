class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lessnode = []
        largenode = []
        current = head
        while current:
            if current.val < x:
                lessnode.append(current)
            else:
                largenode.append(current)
            current = current.next
        
        merged_list = lessnode + largenode
        for n in range(len(merged_list)):
            merged_list[n].next = None
            if n < len(merged_list) - 1:
                merged_list[n].next = merged_list[n+1]
        if len(merged_list) > 0:
            head = merged_list[0]

        return head


        
