# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        nodes_stack = []
        current_depth = 0
        current_value = 0

        for i in range(len(traversal)):
            if traversal[i] == '-':
                current_depth += 1
            else:
                current_value = 10 * current_value + (ord(traversal[i]) - ord('0'))

            if i + 1 == len(traversal) or (traversal[i].isdigit() and traversal[i + 1] == '-'):
                new_node = TreeNode(current_value)

                while len(nodes_stack) > current_depth:
                    nodes_stack.pop()

                if nodes_stack:
                    if nodes_stack[-1].left is None:
                        nodes_stack[-1].left = new_node
                    else:
                        nodes_stack[-1].right = new_node

                nodes_stack.append(new_node)

                current_depth = 0
                current_value = 0
      
        result = None
        while nodes_stack:
            result = nodes_stack.pop()

        return result