# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        deq = deque([root])
        count = 0
        while deq:
            for i in range(len(deq)):
                poped = deq.popleft()
                if poped.left:
                    deq.append(poped.left)
                if poped.right:
                    deq.append(poped.right)
            count += 1
        return count


