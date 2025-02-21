class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        def rec_tree(node):
            self.visited.add(node.val)
            if node.left:
                node.left.val = node.val * 2 + 1
                rec_tree(node.left)
            if node.right:
                node.right.val = node.val * 2 + 2
                rec_tree(node.right)

        root.val = 0
        self.visited = set()
        rec_tree(root)

    def find(self, target: int) -> bool:
        return target in self.visited