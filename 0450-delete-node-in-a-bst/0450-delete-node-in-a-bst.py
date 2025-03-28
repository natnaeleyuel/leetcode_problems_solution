# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                succ = self.findMin(root.right)
                root.val = succ.val
                root.right = self.deleteNode(root.right, succ.val)
        return root
            
    def findMin(self, node: TreeNode) -> TreeNode:
        while node.left:
            node = node.left
        return node
