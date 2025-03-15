class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return []
        
        deq = deque([root])
        l = 0
        while deq:
            curr = []
            nodes = []
            for i in range(len(deq)):
                poped = deq.popleft()
                curr.append(poped.val)
                nodes.append(poped)
                if poped.left:
                    deq.append(poped.left)
                
                if poped.right:
                    deq.append(poped.right)
            
            if l % 2 == 1:
                for i in range(len(nodes)):
                    nodes[i].val = curr.pop()
            l += 1
        return root
