class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        node = root
        while node:
            if node.val > val:
                if not node.left:
                    new_node = TreeNode(val)
                    node.left = new_node
                    return root
                node = node.left
            elif node.val < val:
                if not node.right:
                    new_node = TreeNode(val)
                    node.right = new_node
                    return root
                node = node.right
       