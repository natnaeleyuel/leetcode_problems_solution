# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        while queue:
            for _ in range(len(queue)):
                poped = queue.popleft()
                if poped.left:
                    if poped.val != poped.left.val:
                        return False
                    queue.append(poped.left)
                if poped.right:
                    if poped.val != poped.right.val:
                        return False
                    queue.append(poped.right)
        return True
