class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def preorder(root):
            if not root:
                return 
            
            preorder(root.left)
            preorder(root.right)
            result.append(root.val)
        
        preorder(root)
        return result