class Solution:
    def maxOperations(self, s: str) -> int:
        one_count = 0
        res = 0
        n = len(s)
        i = 0
        while i < n:
            if s[i] == "1":
                one_count += 1
            else:
                res += one_count
                while i + 1 < n and s[i+1] == "0":
                    i += 1
            
            i += 1
        
        return res

