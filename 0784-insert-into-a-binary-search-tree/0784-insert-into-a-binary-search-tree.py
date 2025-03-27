class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def recur(node, num):
            if not node:
                return TreeNode(num)
            
            if num > node.val:
                node.right = recur(node.right, num)
            elif num < node.val:
                node.left = recur(node.left, num)
            
            return node
        
        return recur(root, val)
        
       