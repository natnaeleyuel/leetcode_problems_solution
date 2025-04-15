# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        result = [[root.val]]
        while queue:
            curr = []
            for _ in range(len(queue)):
                poped = queue.popleft()
                if poped.left:
                    left = poped.left
                    curr.append(left.val)
                    queue.append(left)
                if poped.right:
                    right = poped.right
                    curr.append(right.val)
                    queue.append(right)
            if curr:
                result.append(curr)
        return result

