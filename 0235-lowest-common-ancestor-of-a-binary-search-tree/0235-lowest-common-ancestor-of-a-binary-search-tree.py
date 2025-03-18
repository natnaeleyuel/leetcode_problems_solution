# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root
        min_val = min(p.val, q.val)
        max_val = max(p.val, q.val)
        while node:
            if node.val > max_val:
                if node.left:   
                    node = node.left
                else:
                    return node
            elif node.val < min_val:
                if node.right:
                    node = node.right
                else:
                    return node
            elif node.val > min_val and node.val <= max_val:
                return node
            elif node.val >= min_val and node.val < max_val:
                return node
            
        