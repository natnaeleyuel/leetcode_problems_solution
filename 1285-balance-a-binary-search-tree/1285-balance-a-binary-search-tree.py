class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recur(root, arr):
            if not root:
                return 
            
            recur(root.left, arr)
            arr.append(root.val)
            recur(root.right, arr)

        arr = []
        recur(root, arr)

        def balanced_bst(arr, start, end):
            if start > end:
                return None
            
            mid = start + (end - start) // 2

            leftst = balanced_bst(arr, start, mid - 1)
            rightst = balanced_bst(arr, mid+1, end)

            node = TreeNode(arr[mid], leftst, rightst)

            return node
        
        return balanced_bst(arr, 0, len(arr) - 1)