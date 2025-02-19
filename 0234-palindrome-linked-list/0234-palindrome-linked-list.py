class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        current = head
        count = 0
        arr = []
        while current:
            arr.append(current.val)
            current = current.next
        
        return arr == arr[::-1]
        
