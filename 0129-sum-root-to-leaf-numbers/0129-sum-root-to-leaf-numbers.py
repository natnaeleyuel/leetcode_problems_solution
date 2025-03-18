# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        deq = deque([[root, str(root.val)]])
        result = 0
        while deq:
            for i in range(len(deq)):
                poped, val = deq.popleft()
                if poped.left:
                    deq.append([poped.left, val + str(poped.left.val)])
                if poped.right:
                    deq.append([poped.right, val + str(poped.right.val)])
                if not poped.right and not poped.left:
                    result += int(val)
        return result