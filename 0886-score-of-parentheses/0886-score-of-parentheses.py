class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for i in range(len(s)):
            curr = s[i]
            if curr == '(':
                stack.append(0)
            else:
                x = stack.pop()
                res = max(1, 2 * x)
                stack[-1] += res
        return stack[-1]