class Solution:
    def isValid(self, s: str) -> bool:
        matching  = {'(':')', '{':'}', '[':']'}
        stack = []
        for i in range(len(s)):
            curr = s[i]
            if curr in matching:
                stack.append(curr)
            elif not stack or matching[stack.pop()] != curr:
                return False
        return not stack 