class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""

        s_set = set(s)

        for i in range(len(s)):
            curr = s[i]
            if curr.swapcase() in s_set:
                continue
            left = self.longestNiceSubstring(s[:i])
            right = self.longestNiceSubstring(s[i+1:])

            return left if len(left) >= len(right) else right
        return s