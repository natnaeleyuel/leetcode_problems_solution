
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def recur(node, num):
            if not node:
                return None
            elif node.val == val:
                return node
            elif node.val > val:
                return recur(node.left, num)
            elif node.val < val:
                return recur(node.right, num)
        
        return recur(root, val)