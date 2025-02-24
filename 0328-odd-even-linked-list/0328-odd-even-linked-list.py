# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        listone = []
        listtwo = []
        count = 0
        current = head
        while current:
            if count % 2 == 0:
                listone.append(current)
            else:
                listtwo.append(current)
            current = current.next
            count += 1
        
        mergelist = listone + listtwo
        for i in range(len(mergelist)):
            mergelist[i].next = None
            if i < len(mergelist) - 1:
                mergelist[i].next = mergelist[i+1]
        
        if len(mergelist) > 0:
            mergelist[0] = head
        return head