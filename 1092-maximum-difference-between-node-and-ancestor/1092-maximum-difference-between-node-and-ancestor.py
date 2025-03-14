class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def recur(root, minval, maxval):
            if not root:
                return 0
            
            curr = max(abs(root.val - minval), abs(root.val - maxval))

            minval = min(minval, root.val)
            maxval = max(maxval, root.val)

            return max(curr, recur(root.left, minval, maxval),  recur(root.right, minval, maxval))       
        
        return recur(root, root.val, root.val)