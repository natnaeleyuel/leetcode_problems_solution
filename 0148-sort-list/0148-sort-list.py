# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        arr.sort()
        head = ListNode(arr[0])
        curr = head
        for i in range(1, len(arr)):
            new_node = ListNode(arr[i])
            curr.next = new_node
            curr = new_node
        
        return head

