class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        dummy = ListNode()
        node.val = node.next.val
        node.next = node.next.next
        
        return dummy.next

        