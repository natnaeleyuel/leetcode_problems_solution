class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def preorder(root):
            if not root:
                return 
            
            result.append(root.val)
            preorder(root.left)
            preorder(root.right)
        
        preorder(root)
        return result