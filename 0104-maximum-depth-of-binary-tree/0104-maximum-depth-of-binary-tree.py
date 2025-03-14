# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def depthfind(root):
            if not root:
                return 0
            
            left = depthfind(root.left)
            right = depthfind(root.right)
            return max(left, right) + 1
        
        return depthfind(root)


