class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        deq = deque([root])
        count = 1
        result = []
        while deq:
            curr = []
            for i in range(len(deq)):
                poped = deq.popleft()
                curr.append(poped.val)
                if poped.left:
                    deq.append(poped.left)
                if poped.right:
                    deq.append(poped.right)
            count += 1
            if count % 2 == 0:
                result.append(curr)
            else:
                result.append(curr[::-1])
        return result