class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(s, result, start, curr):
            if start > 4:
                return 
            
            if start == 4 and not s:
                result.append(curr[:-1])
            
            for i in range(1, len(s) + 1):
                if s[:i] == '0' or (s[0] != '0' and 0 < int(s[:i]) < 256):
                    backtrack(s[i:], result, start + 1, curr + s[:i] + '.')
            
        result = []
        backtrack(s, result, 0, '')
        return result