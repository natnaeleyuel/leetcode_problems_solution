class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        current = head
        new_list = []
        
        while current:
            new_list.append(current)
            current = current.next
        
        nodelist = []
        for i in range(0, len(new_list), k):
            group = new_list[i:i+k]
            if len(group) == k:
                nodelist.extend(group[::-1])  
            else:
                nodelist.extend(group)  
        
        for c in range(len(nodelist)):
            nodelist[c].next = None
            if c < len(nodelist) - 1:
                nodelist[c].next = nodelist[c+1]
        
        dummy.next = nodelist[0] if nodelist else None
        return dummy.next