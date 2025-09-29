# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return 0, 0
            
            left_robe, left_skip = dfs(node.left)
            right_robe, right_skip = dfs(node.right)

            curr_robe = node.val + left_skip + right_skip
            curr_skip = max(left_robe, left_skip) + max(right_robe, right_skip)

            return curr_robe, curr_skip
        
        return max(dfs(root))