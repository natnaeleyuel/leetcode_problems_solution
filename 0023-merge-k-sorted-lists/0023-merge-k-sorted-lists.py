# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        n = len(lists)
        for i in range(n):
            root = lists[i]
            curr = root
            while curr:
                heappush(heap, curr.val)
                if curr.next:
                    curr = curr.next
                else:
                    break
            
        if not heap:
            return None
        prev = ListNode(heappop(heap))
        root = prev
        while heap:
            curr = ListNode(heappop(heap))
            prev.next = curr
            prev = curr
        
        return root

        



