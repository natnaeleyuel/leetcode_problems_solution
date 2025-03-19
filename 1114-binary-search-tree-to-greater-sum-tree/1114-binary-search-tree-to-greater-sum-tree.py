# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        deq = deque([root])
        arr = [root]
        while deq:
            for i in range(len(deq)):
                poped = deq.popleft()
                if poped.left:
                    deq.append(poped.left)
                    arr.append(poped.left)
                if poped.right:
                    deq.append(poped.right)
                    arr.append(poped.right)
        arr = sorted(arr, key = lambda node: node.val, reverse = True)
        for i in range(1, len(arr)):
            node = arr[i]
            node.val += arr[i-1].val

        return root