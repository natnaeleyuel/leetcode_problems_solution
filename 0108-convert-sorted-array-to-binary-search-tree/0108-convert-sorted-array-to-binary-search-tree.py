# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def recur(arr, left, right):
            if left > right:
                return None
            mid = left + (right - left) // 2
            node = TreeNode(arr[mid])
            node.left = recur(arr, left, mid - 1)
            node.right = recur(arr, mid + 1, right)
            return node
        
        n = len(nums)
        if n == 0:
            return None
        return recur(nums, 0, n - 1)