class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        deq = deque([root])
        result = []
        while deq:
            maxval = -float('inf')
            for i in range(len(deq)):
                poped = deq.popleft()
                maxval = max(maxval, poped.val)
                
                if poped.left:
                    deq.append(poped.left)
                
                if poped.right:
                    deq.append(poped.right)
            
            result.append(maxval)
        
        return result

