
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        deq = deque([root])
        node = None
        while deq:
            for i in range(len(deq)):
                poped = deq.popleft()
                if poped.val == val:
                    node = poped
                if poped.left:
                    deq.append(poped.left)
                if poped.right:
                    deq.append(poped.right)
       
        return node