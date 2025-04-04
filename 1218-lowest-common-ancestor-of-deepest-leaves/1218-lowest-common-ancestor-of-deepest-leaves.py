# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        deq = deque([root])
        dpl = []
        while deq:
            dpl = list(deq)
            for i in range(len(deq)):
                poped = deq.popleft()
                if poped.left:
                    deq.append(poped.left)
                if poped.right:
                    deq.append(poped.right)

        if len(dpl) == 1:
            return dpl[0]

        def helper(node, l, r):
            if not node or node == l or node == r:
                return node
            left = helper(node.left, l, r)
            right = helper(node.right, l, r)
            if left and right:
                return node
            
            return left if left else right
        
        k = dpl[0]
        for node in dpl[1:]:
            k = helper(root, k, node)
        
        return k



