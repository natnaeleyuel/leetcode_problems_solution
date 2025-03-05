class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        l = max(len(s), len(t))
        for i in range(l):
            if i < len(s):
                curr = s[i]
                if curr != '#':
                    stack1.append(curr)
                elif stack1:
                    stack1.pop()
            if i < len(t):
                curr = t[i]
                if curr != '#':
                    stack2.append(curr)
                elif stack2:
                    stack2.pop()
        return stack1 == stack2