# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        nodeList = []
        resultList = []
        while head:
            nodeList.append(head.val)
            head = head.next
        
        m = len(nodeList)
        while m > 0:
            resultList.append(nodeList[m-1] + nodeList[-m])
            m -= 1
        
        return max(resultList)